import json
from bson.objectid import ObjectId
from flask import Blueprint, Response, request
from pymongo.collection import ReturnDocument
from functools import wraps
from .. import auth
from routes.database import db

inventory = Blueprint('inventory', __name__)

BUY_ACTION = "buy"
SELL_ACTION = "sell"

########################################
# Get all items in a user's inventory
@inventory.route("/inventory", methods=["GET"])
@auth.auth_required
def get_all_inventory_items(current_user):
  try:
    return Response(response=json.dumps({"inventory": current_user["inventory"]}), status=200, mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Inventory items cannot be retrieved"}), status=500, mimetype="application/json")

########################################
# To buy an item from the store, and add it into user's inventory
def buy_inventory_item(store_item_id, current_user):
  try:
    # Fetch user's inventory
    inventory = current_user["inventory"]

    # Fetch store item from db
    store_item_to_buy = db.store.find_one({"_id": ObjectId(store_item_id)})

    # If user's money < item.buyPrice, return error, 403 forbidden
    money = int(current_user["money"])
    item_price = int(store_item_to_buy["buyPrice"])
    if money < item_price:
      return Response(response=json.dumps({"message": "Insufficient money to buy the item"}), status=403, mimetype="application/json")
    
    # If store item is in user's inventory, increment quantity by 1
    item_found = False
    for item in inventory:
      if item["store_item_id"] == store_item_id:
        item_found = True
        item["quantity"] += 1

    # If store item not in user's inventory, add it with quantity 1
    if not item_found:
      new_inventory_item = {
        "store_item_id": store_item_id,
        "itemName": store_item_to_buy["itemName"],
        "sellPrice": store_item_to_buy["buyPrice"],
        "quantity": 1,
        "base64Img": store_item_to_buy["base64Img"],
      }
      inventory.append(new_inventory_item)
    
    # Deduct money by store item.buyPrice
    new_money = money - item_price

    # Update user info in database
    user_id = current_user["_id"]
    updated_user = db.users.find_one_and_update(
      {"_id": user_id}, 
      {
        "$set": {
          "inventory": inventory,
          "money": new_money
        }
      }, return_document=ReturnDocument.AFTER)

    # Display inventory without image
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

# Sells and item from user's inventory
def sell_inventory_item(store_item_id, current_user):
  try:
    # Retrieve user's inventory
    inventory = current_user["inventory"]

    # Look for item in user's inventory
    sell_price = 0
    item_found = False
    for item in inventory:
      if item["store_item_id"] == store_item_id:
        item_found = True
        sell_price = int(item["sellPrice"])
        # If quantity is 1, remove item from inventory
        if (item["quantity"] == 1):
          inventory.remove(item)
        # If quantity is more than 1, decrement quantity by 1
        elif (item["quantity"] > 1):
          item["quantity"] -= 1

    # If store item id is not in user's inventory, throw error
    if (not item_found):
      return Response(response=json.dumps({"message": "Inventory item you are trying to sell is not owned"}), status=403, mimetype="application/json")
    
    # Increment user's money by sell price
    new_money = int(current_user["money"]) + sell_price

    # Update user info in database
    user_id = current_user["_id"]
    updated_user = db.users.find_one_and_update(
      {"_id": user_id}, 
      {
        "$set": {
          "inventory": inventory,
          "money": new_money
        }
      }, return_document=ReturnDocument.AFTER)

    # Display inventory without image
    inventory_display = updated_user["inventory"]
    for item in inventory_display:
      item.pop('base64Img')

    return Response(response=json.dumps({
      "money": updated_user["money"],
      "inventory": inventory_display,
      }), status=200, mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "Inventory item cannot be sold"}), status=500, mimetype="application/json")

# Checks whether item is to be bought or sold and calls respective helper function
@inventory.route("/inventoryItem", methods=["POST"])
@auth.auth_required
def inventory_item(current_user):
  store_item_id = request.form["itemId"]
  if (request.form["action"] == BUY_ACTION):
    return buy_inventory_item(store_item_id=store_item_id, current_user=current_user)
  elif (request.form["action"] == SELL_ACTION):
    return sell_inventory_item(store_item_id=store_item_id, current_user=current_user)
