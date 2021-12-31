import json
import os
from flask import Blueprint, Response, request
from passlib.hash import pbkdf2_sha256
from dotenv import load_dotenv
from .. import utils
from .. import auth
from routes.database import db

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
    existing_users_with_username = list(db.users.find({"username": request.form["username"]}))
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
      response=json.dumps( # send object as a json
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
    access_token = auth.create_access_token({"_id": str(user["_id"])}) # convert objectId to string since objectId is not json serializable
    token = access_token["token"]
    expiry = access_token["expiry"]

    # Attach token as cookie
    res = Response(response=json.dumps({"message": "Token successfully created"}), status=200, mimetype="application/json")
    res.set_cookie(key="jwt", value=token, expires=expiry, httponly=True) # cookie expiry same as jwt token expiry
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
    current_user["_id"] = str(current_user["_id"]) # convert objectId to string to allow it to be JSON serializable

    return Response(response=json.dumps({"data": current_user}), status=200, mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "User cannot be retrieved"}), status=500, mimetype="application/json")

########################################
# To sign a user out, and delete jwt cookie
@user.route("/session", methods=["DELETE"])
@auth.auth_required
def signout(current_user):
  try:
    res = Response(response=json.dumps({"message": "Token successfully deleted, user logged out."}), status=200, mimetype="application/json")
    res.set_cookie(key='jwt', value='')

    return res
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "User cannot be logged out"}), status=500, mimetype="application/json")