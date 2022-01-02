import json
from flask import Blueprint, Response, request
from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument
from .. import auth
from routes.database import db

money = Blueprint('money', __name__)

########################################
# To update a user's money
@money.route("/money", methods=["POST"])
@auth.auth_required
def add_money(current_user):
  try:
    id = ObjectId(current_user["_id"])
    
    updated_item = db.users.find_one_and_update(
      {"_id": id},
      {"$set": { "money": request.form["money"]}},
      return_document=ReturnDocument.AFTER
    )
    return Response(response=json.dumps(
        {
          "username": updated_item['username'],
          "password": updated_item['password'],
          "money": updated_item['money'],
          "inventory": updated_item['inventory']
        }
      ), status=200, mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Money cannot be updated"}), status=500, mimetype="application/json")

########################################
# To fetch a user's money
@money.route("/money", methods=["GET"])
@auth.auth_required
def get_money(current_user):
  try:
    id = ObjectId(current_user["_id"])
    
    user = db.users.find_one({"_id": id})
    return Response(response=json.dumps({"money": user['money']}), status=200, mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Money cannot be updated"}), status=500, mimetype="application/json")