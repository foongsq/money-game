import json
import base64
from flask import Blueprint, Response, request
from bson.objectid import ObjectId
from .. import utils
from routes.database import db

store = Blueprint('store', __name__)

########################################
# To add an item to the store
@store.route("/storeItem", methods=["POST"])
def add_store_item():
  try:
    img = request.files["img"]
    b64_img = base64.b64encode(img.read()).decode('utf-8')
    storeItem = {
      "itemName": request.form["itemName"],
      "base64Img": b64_img, 
      "buyPrice": request.form["buyPrice"],
    }
    inserted_item = utils.insert_item_into_store(storeItem)
    return Response(
      response=json.dumps(
        {
          "itemName": inserted_item['itemName'],
          "buyPrice": inserted_item['buyPrice'],
          "base64Img": inserted_item['base64Img'],
        }
      ), 
      status=200, mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Store item cannot be added"}), status=500, mimetype="application/json")

########################################
# To get all items in the store
@store.route("/store", methods=["GET"])
def get_all_store_items():
  try:
    store_items = list(db.store.find())
    for item in store_items: # convert object id to string since object id is not json serializable
      item["_id"] = str(item["_id"])
    return Response(response=json.dumps(store_items), status=200, mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Store items cannot be retrieved"}), status=500, mimetype="application/json")

########################################
# To get delete an item from the store
@store.route("/storeItem/<id>", methods=["DELETE"])
def delete_store_item(id):
  try:
    deleted_item = db.store.find_one_and_delete({"_id": ObjectId(id)})
    return Response(
      response=json.dumps(
        {
          "message": "Store item successfully deleted",
          "_id": deleted_item['_id'],
          "itemName": deleted_item['itemName'],
          "buyPrice": deleted_item['itemName'],
        }), 
      status=200, mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Store item cannot be deleted"}), status=500, mimetype="application/json")