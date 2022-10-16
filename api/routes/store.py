import json
import base64
from flask import Blueprint, Response, request
from bson.objectid import ObjectId
import utils
import auth
from database import db

store = Blueprint('store', __name__)

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
# To add an item to the store
@store.route("/storeItem", methods=["POST"])
@auth.admin_required
def add_store_item(admin):
  try:
    img = request.files["img"]
    b64_img = base64.b64encode(img.read()).decode('utf-8')
    
    storeItem = {
      "itemName": request.form["itemName"],
      "base64Img": b64_img, 
      "price": request.form["price"],
    }
    inserted_item = utils.insert_item_into_store(storeItem)
    return Response(
      response=json.dumps(
        {
          "_id": str(inserted_item['_id']),
          "itemName": inserted_item['itemName'],
          "price": inserted_item['price'],
          "base64Img": inserted_item['base64Img'],
        }
      ), 
      status=200, mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Store item cannot be added"}), status=500, mimetype="application/json")

########################################
# To get delete an item from the store
@store.route("/storeItem/<id>", methods=["DELETE"]) # delete requests dont support request body
@auth.admin_required
def delete_store_item(admin, id):
  try:
    print(id)
    deleted_item = db.store.find_one_and_delete({"_id": ObjectId(id)})
    return Response(
      response=json.dumps(
        {
          "_id": str(deleted_item['_id']),
          "itemName": deleted_item['itemName'],
          "price": deleted_item['price'],
        }), 
      status=200, mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Store item cannot be deleted"}), status=500, mimetype="application/json")