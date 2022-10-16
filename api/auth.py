import jwt
import json
import os
from flask import Response, request
from bson.objectid import ObjectId
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from functools import wraps
from database import db

load_dotenv()

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
ADMIN_ID = os.getenv('ADMIN_ID')

# Creates a JWT token according to id of user


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = (datetime.now() + timedelta(minutes=60)).timestamp()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY,
                             algorithm=JWT_ALGORITHM)
    return {"token": encoded_jwt, "expiry": expire}

# Decodes JWT token and returns current user


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        id: str = payload.get("_id")
        if id is None:
            return Response(response=json.dumps({"message": "ID in token invalid"}), status=401, mimetype="application/json")

        current_user = db.users.find_one({"_id": ObjectId(id)})
        return current_user
    except Exception as ex:
        print(ex)
        return Response(response=json.dumps({"message": "JWT Error"}), status=500, mimetype="application/json")

# Decorator for checking whether valid jwt exists


def auth_required(f):
    @ wraps(f)
    def decorated(*args, **kwargs):
        try:
            jwt = None
            # jwt is passed in the request header
            if 'x-access-token' in request.headers:
                jwt = request.headers['x-access-token']

            if (jwt is None or jwt == ''):
                return Response(response=json.dumps({"message": "User is not logged in"}), status=401, mimetype="application/json")

            current_user = verify_access_token(jwt)
        except:
            return Response(response=json.dumps({"message": "Token is invalid"}), status=401, mimetype="application/json")
        # returns the current logged in users context to the routes
        return f(current_user, *args, **kwargs)
    return decorated

# Decorator for checking whether valid jwt exists and that admin is logged in


def admin_required(f):
    @ wraps(f)
    def decorated(*args, **kwargs):
        try:
            jwt = None
            # jwt is passed in the request header
            if 'x-access-token' in request.headers:
                jwt = request.headers['x-access-token']

            if (jwt is None or jwt == ''):
                return Response(response=json.dumps({"message": "Admin is not logged in"}), status=401, mimetype="application/json")

            current_user = verify_access_token(jwt)

            # Checks if current user is admin
            if (str(current_user["_id"]) != ADMIN_ID):
                return Response(response=json.dumps({"message": "Unauthorized access, only admins can access this resource"}), status=401, mimetype="application/json")
        except:
            return Response(response=json.dumps({"message": "Token is invalid"}), status=401, mimetype="application/json")
        # returns the current logged in users context to the routes
        return f(current_user, *args, **kwargs)
    return decorated
