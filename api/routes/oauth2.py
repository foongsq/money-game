import jwt
import json
import os
from flask import Response, request
from bson.objectid import ObjectId
from functools import wraps
from dotenv import load_dotenv
from datetime import datetime, timedelta
from routes.database import db

load_dotenv()

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
JWT_EXPIRY_MIN = os.getenv('JWT_EXPIRY_MIN')

# decorator for verifying the JWT
def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    token = None
    # jwt is passed in the request header
    if 'Authentication' in request.headers:
      token = request.headers['Authentication']
    # return 401 if token is not passed
    if not token:
      return Response(response=json.dumps({"message": "Token not found"}), status=401, mimetype="application/json")

    try:
      # decoding the payload to fetch the stored details
      data = jwt.decode(token, JWT_SECRET_KEY)
      current_user = db.users.find_one({"_id": ObjectId(data["id"])})
    except:
      return Response(response=json.dumps({"message": "Token is invalid"}), status=401, mimetype="application/json")
    # returns the current logged in users contex to the routes
    return  f(current_user, *args, **kwargs)

  return decorated

def create_access_token(data: dict):
  to_encode = data.copy()

  expire = datetime.now() + timedelta(minutes=int(JWT_EXPIRY_MIN))
  to_encode.update({"exp": expire})

  encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
  return encoded_jwt

