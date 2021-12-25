from flask import Blueprint, Response, request
import json
from pymongo.collection import ReturnDocument
from routes.database import db

money_blueprint = Blueprint('money_blueprint', __name__)

########################################
# To update a user's money
@money_blueprint.route("/money", methods=["POST"])
def add_money():
  try:
    updated_item = db.users.find_one_and_update(
      {"username": request.form["username"]},
      {"$set": { "money": request.form["money"]}},
      return_document=ReturnDocument.AFTER
    )
    return Response(
      response=json.dumps( # send object as a json
        {
          "message": "Money succesfully updated", 
          "username": f"{updated_item['username']}",
          "password": f"{updated_item['password']}",
          "money": f"{updated_item['money']}",
          "inventory": f"{updated_item['inventory']}"
        }
      ), 
      status=200, 
      mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Money cannot be updated"}), status=500, mimetype="application/json")