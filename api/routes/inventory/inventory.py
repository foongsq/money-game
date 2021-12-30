import json
from bson.objectid import ObjectId
from flask import Blueprint, Response, request
from pymongo.collection import ReturnDocument
from .. import utils
from .. import oauth2
from routes.database import db

inventory = Blueprint('inventory', __name__)

########################################
# Get all items in a user's inventory
@inventory.route("/inventory", methods=["GET"])
def get_all_inventory_items():
  try:
    jwt = request.cookies.get("jwt")
    current_user = oauth2.verify_access_token(jwt)

    return Response(response=json.dumps({"inventory": current_user["inventory"]}), status=200, mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Inventory items cannot be retrieved"}), status=500, mimetype="application/json")

########################################
# To buy an item from the store, and add it into user's inventory
@inventory.route("/inventoryItem/buy/<storeItemId>", methods=["POST"])
def buy_inventory_item(storeItemId):
  try:
    # Fetch user's inventory
    jwt = request.cookies.get("jwt")
    current_user = oauth2.verify_access_token(jwt)
    inventory = current_user["inventory"]

    # Fetch store item from db
    store_item_to_buy = db.store.find_one({"_id": ObjectId(storeItemId)})

    # if user's money < item.buyPrice, return error, 403 forbidden
    money = int(current_user["money"])
    item_price = int(store_item_to_buy["buyPrice"])
    if money < item_price:
      return Response(response=json.dumps({"message": "Insufficient money to buy the item"}), status=403, mimetype="application/json")
    
    # if store item is in user's inventory, increment quantity by 1
    item_found = False
    for item in inventory:
      if item["store_item_id"] == storeItemId:
        item_found = True
        item["quantity"] += 1

    # if store item not in user's inventory, add it with quantity 1
    if not item_found:
      new_inventory_item = {
        "store_item_id": storeItemId,
        "itemName": store_item_to_buy["itemName"],
        "sellPrice": store_item_to_buy["buyPrice"],
        "quantity": 1,
        "base64Img": store_item_to_buy["base64Img"],
      }
      inventory.append(new_inventory_item)
    
    # deduct money by store item.buyPrice
    new_money = money - item_price

    # update user info in database
    user_id = current_user["_id"]
    updated_user = db.users.find_one_and_update(
      {"_id": user_id}, 
      {
        "$set": {
          "inventory": inventory,
          "money": new_money
        }
      }, return_document=ReturnDocument.AFTER)

    # display inventory without image
    inventory_display = updated_user["inventory"]
    for item in inventory_display:
      item.pop('base64Img')

    return Response(response=json.dumps({
      "money": updated_user["money"],
      "inventory": inventory_display,
      }), status=200, mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Store item cannot be bought"}), status=500, mimetype="application/json")