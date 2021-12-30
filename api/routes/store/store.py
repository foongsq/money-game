from flask import Blueprint, Response, request
import json
from bson.objectid import ObjectId
import base64

from .. import utils
from routes.database import db

store_blueprint = Blueprint('store_blueprint', __name__)

########################################
# To add an item to the store
@store_blueprint.route("/storeItem", methods=["POST"])
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
          "message": "Store item succesfully added", 
          "itemName": f"{inserted_item['itemName']}",
          "base64Img": f"{inserted_item['base64Img']}",
          "buyPrice": f"{inserted_item['buyPrice']}",
        }
      ), 
      status=200, 
      mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Store item cannot be added"}), status=500, mimetype="application/json")

########################################
# To get all items in the store
@store_blueprint.route("/store", methods=["GET"])
def get_all_store_items():
  try:
    store_items = list(db.store.find())
    for item in store_items: # convert object id to string since object id is not json serializable
      item["_id"] = str(item["_id"])
    return Response(
      response=json.dumps(store_items), 
      status=200, 
      mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Store items cannot be retrieved"}), status=500, mimetype="application/json")

########################################
# To get delete an item from the store
@store_blueprint.route("/storeItem/<id>", methods=["DELETE"])
def delete_store_item(id):
  try:
    deleted_item = db.store.find_one_and_delete({"_id": ObjectId(id)})
    return Response(
      response=json.dumps(
        {
          "message": "Store item successfully deleted",
          "_id": f"{deleted_item['_id']}",
          "itemName": f"{deleted_item['itemName']}",
          "buyPrice": f"{deleted_item['itemName']}",
        }), 
      status=200, 
      mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Store item cannot be deleted"}), status=500, mimetype="application/json")