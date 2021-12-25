from flask import Flask, Response, request
from flask_cors import CORS
import pymongo # To connect flask app to mongodb
import json
from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument
import base64
from passlib.hash import pbkdf2_sha256

# Helper methods

# Inserts an item into users db and returns the inserted item
def insert_item_into_users(item):
  db_response = db.users.insert_one(item)
  inserted_item = db.users.find_one(db_response.inserted_id)
  return inserted_item

# Inserts an item into store db and returns the inserted item
def insert_item_into_store(item):
  db_response = db.store.insert_one(item)
  inserted_item = db.store.find_one(db_response.inserted_id)
  return inserted_item

# Create a flask app
app = Flask(__name__)
cors = CORS(app, resources={r"/*": { "origins": "http://localhost:8080"}}) # allow frontend to access API

# Connect to mongodb (always wrap connection in try except block)
try:
  mongo = pymongo.MongoClient(
    host="localhost", 
    port=27017, # default TCP port used by mongodb
    serverSelectionTimeoutMS=1000 # if cannot connect in 1000ms, means connection failed
  )
  db = mongo.moneygame # access database named moneygame
  mongo.server_info() # trigger exception if connection fails
except: 
  print("Error - Cannot connect to db")

########################################
# To add a new user (with username, password, and 0 money, 
# and empty inventory) into the database
@app.route("/user", methods=["POST"])
def signup():
  try:
    # Hash password
    hashed_password = pbkdf2_sha256.hash(request.form["password"])
    
    # Ensure that username is unique
    existing_users_with_username = list(db.users.find({"username": request.form["username"]}))
    if (len(existing_users_with_username) > 0):
      return Response(response=json.dumps({"message": "Username already exists in database"}), status=409, mimetype="application/json")
    
    user = {
      "username": request.form["username"], 
      "password": hashed_password,
      "money": 0,
      "inventory": [],
    }

    inserted_item = insert_item_into_users(user)

    return Response(
      response=json.dumps( # send object as a json
        {
          "message": "User created successfully", 
          "username": f"{inserted_item['username']}",
          "password": f"{inserted_item['password']}",
          "money": f"{inserted_item['money']}",
          "inventory": f"{inserted_item['inventory']}"
        }
      ), 
      status=200, 
      mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "User cannot be created"}), status=500, mimetype="application/json")

########################################
# To get all user's data from the database
@app.route("/user", methods=["GET"])
def signin():
  try:
    input_password = request.form["password"]
    user = db.users.find_one({"username": request.form["username"]})
    
    if (user == None):
      return Response(response=json.dumps({"message": "Username incorrect"}), status=403, mimetype="application/json")
    
    if (not pbkdf2_sha256.verify(input_password,  user["password"])):
      return Response(response=json.dumps({"message": "Password incorrect"}), status=403, mimetype="application/json")

    return Response(
      response=json.dumps( # send object as a json
        {
          "username": user["username"],
          "money": user["money"],
          "inventory": user["inventory"],
        }
      ), 
      status=200, 
      mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(response=json.dumps({"message": "User cannot be retrieved"}), status=500, mimetype="application/json")

########################################
# To update a user's money
@app.route("/money", methods=["POST"])
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

########################################
# To add an item to the store
@app.route("/storeItem", methods=["POST"])
def add_store_item():
  try:
    img = request.files["img"]
    b64_img = base64.b64encode(img.read()).decode('utf-8')
    storeItem = {
      "itemName": request.form["itemName"],
      "base64Img": b64_img, 
      "buyPrice": request.form["buyPrice"],
    }
    inserted_item = insert_item_into_store(storeItem)
    return Response(
      response=json.dumps( # send object as a json
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
@app.route("/store", methods=["GET"])
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
@app.route("/storeItem/<id>", methods=["DELETE"])
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

########################################
# To buy an item from the store, and add it into user's inventory
# @app.route("/inventoryItem/buy/<id>", methods=["POST"])
# def buy_inventory_item(id):
#   try:
#     img = request.files["img"]
#     b64_img = base64.b64encode(img.read()).decode('utf-8')
#     storeItem = {
#       "itemName": request.form["itemName"],
#       "base64Img": b64_img, 
#       "buyPrice": request.form["buyPrice"],
#     }
#     inserted_item = insert_item_into_store(storeItem)
#     return Response(
#       response=json.dumps( # send object as a json
#         {
#           "message": "Store item succesfully added", 
#           "itemName": f"{inserted_item['itemName']}",
#           "base64Img": f"{inserted_item['base64Img']}",
#           "buyPrice": f"{inserted_item['buyPrice']}",
#         }
#       ), 
#       status=200, 
#       mimetype="application/json")
#   except Exception as ex:
#     print(ex)
#     return Response(response=json.dumps({"message": "Store item cannot be added"}), status=500, mimetype="application/json")

########################################
# Run your flask app on port 80
if __name__ == "__main__":
  app.run(port=80, debug=True)