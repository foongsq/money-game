import jwt
import json
import os
from flask import Response
from bson.objectid import ObjectId
from dotenv import load_dotenv
from datetime import datetime, timedelta
from routes.database import db

load_dotenv()

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
JWT_EXPIRY_MIN = os.getenv('JWT_EXPIRY_MIN')

# Creates a JWT token according to id of user
def create_access_token(data: dict):
  to_encode = data.copy()

  expire = datetime.now() + timedelta(minutes=int(JWT_EXPIRY_MIN))
  to_encode.update({"exp": expire})

  encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
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
  except:
    return Response(response=json.dumps({"message": "JWT Error"}), status=500, mimetype="application/json") 
