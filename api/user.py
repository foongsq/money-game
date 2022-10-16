import json
import os
import sys
from flask import Blueprint, Response, request
from passlib.hash import pbkdf2_sha256
from dotenv import load_dotenv
import utils
import auth
from database import db

load_dotenv()
JWT_EXPIRY_MIN = os.getenv('JWT_EXPIRY_MIN')

user = Blueprint('user', __name__)

########################################
# To add a new user (with username, password, and 0 money,
# and empty inventory) into the database


@user.route("/user", methods=["POST"])
def signup():
    try:
        # Hash password
        hashed_password = pbkdf2_sha256.hash(request.form["password"])

        # Ensure that username is unique
        existing_users_with_username = list(
            db.users.find({"username": request.form["username"]}))
        if (len(existing_users_with_username) > 0):
            return Response(response=json.dumps({"message": "Username already exists in database"}), status=409, mimetype="application/json")

        user = {
            "username": request.form["username"],
            "password": hashed_password,
            "money": 0,
            "inventory": [],
        }

        inserted_item = utils.insert_item_into_users(user)

        return Response(
            response=json.dumps(  # send object as a json
                {
                    "message": "User created successfully",
                    "username": f"{inserted_item['username']}",
                    "password": f"{inserted_item['password']}",
                    "money": f"{inserted_item['money']}",
                    "inventory": f"{inserted_item['inventory']}"
                }
            ),
            status=200,
            mimetype="application/json")
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message": "User cannot be created"}), status=500, mimetype="application/json")

########################################
# To get jwt access token


@user.route("/session", methods=["POST"])
def signin():
    try:
        input_password = request.form["password"]
        user = db.users.find_one({"username": request.form["username"]})

        # Check if username exists in database
        if (user == None):
            return Response(response=json.dumps({"message": "Username incorrect"}), status=403, mimetype="application/json")

        # Check if password matches the one stored in database
        if (not pbkdf2_sha256.verify(input_password,  user["password"])):
            return Response(response=json.dumps({"message": "Password incorrect"}), status=403, mimetype="application/json")

        # Create jwt access token with objectId of user document
        print(user["_id"])
        # convert objectId to string since objectId is not json serializable
        access_token = auth.create_access_token({"_id": str(user["_id"])})
        token = access_token["token"]
        expiry = access_token["expiry"]

        res = Response(response=json.dumps({"message": "Token successfully created",
                       "token": token, "expiry": expiry}), status=200, mimetype="application/json")
        print('token set', token)
        return res
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message": "User cannot be retrieved"}), status=500, mimetype="application/json")

########################################
# To get all user data for user who is signed in


@user.route("/session", methods=["GET"])
@auth.auth_required
def get_user(current_user):
    try:
        # convert objectId to string to allow it to be JSON serializable
        current_user["_id"] = str(current_user["_id"])
        print(current_user)
        return Response(response=json.dumps({"data": current_user}), status=200, mimetype="application/json")
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message": "User cannot be retrieved"}), status=500, mimetype="application/json")
