import json
from flask import Blueprint, Response, request
from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument
from .. import oauth2
from routes.database import db

money = Blueprint('money', __name__)

########################################
# To update a user's money
@money.route("/money", methods=["POST"])
def add_money():
  try:
    jwt = request.cookies.get("jwt")

    # Check if jwt token in cookie exists
    if (jwt is None or jwt is ''):
      return Response(response=json.dumps({"message": "User is not logged in"}), status=401, mimetype="application/json")
    
    current_user = oauth2.verify_access_token(jwt)
    id = ObjectId(current_user["_id"])
    
    updated_item = db.users.find_one_and_update(
      {"_id": id},
      {"$set": { "money": request.form["money"]}},
      return_document=ReturnDocument.AFTER
    )
    return Response(
      response=json.dumps( # send object as a json
        {
          "username": updated_item['username'],
          "password": updated_item['password'],
          "money": updated_item['money'],
          "inventory": updated_item['inventory']
        }
      ), 
      status=200, 
      mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Money cannot be updated"}), status=500, mimetype="application/json")