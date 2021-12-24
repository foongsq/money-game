from flask import Flask, Response, request
import pymongo # To connect flask app to mongodb
import json
from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument
import gridfs

# import os
# from dotenv import load_dotenv, find_dotenvload_dotenv(find_dotenv())
# os.getenv('SECRET_KEY')

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

# Connect to mongodb (always wrap connection in try except block)
try:
  mongo = pymongo.MongoClient(
    host="localhost", 
    port=27017, # default TCP port used by mongodb
    serverSelectionTimeoutMS=1000 # if cannot connect in 1000ms, means connection failed
  )
  db = mongo.moneygame # access database named moneygame
  fs = gridfs.GridFS(db)
  mongo.server_info() # trigger exception if connection fails
except: 
  print("Error - Cannot connect to db")

########################################
# To add a new user (with username, password, and 0 money, 
# and empty inventory) into the database
# TODO: Make sure username is not already in the database
@app.route("/user", methods=["POST"])
def signup():
  try:
    user = {
      "username": request.form["username"], 
      "password": request.form["password"],
      "money": 0,
      "inventory": [],
    }
    inserted_item = insert_item_into_users(user)
    # for attr in dir(db_response):
      # print(attr)
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

########################################
# To get all user's data from the database
@app.route("/user", methods=["GET"])
def signin():
  try:
    data = list(db.users.find({"username": request.form["username"]}))
    return Response(
      response=json.dumps( # send object as a json
        {
          "username": data[0]["username"],
          "password": data[0]["password"],
          "money": data[0]["money"],
          "inventory": data[0]["inventory"],
        }
      ), 
      status=200, 
      mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(
      response=json.dumps( # send object as a json
        {
          "message": "User cannot be retrieved", 
        }
      ), 
      status=500, 
      mimetype="application/json")

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
    return Response(
      response=json.dumps( # send object as a json
        {
          "message": "Money cannot be updated", 
        }
      ), 
      status=500, 
      mimetype="application/json")

########################################
# To add an item to the store
@app.route("/storeItem", methods=["POST"])
def add_store_item():
  try:
    img = request.files["img"]
    img_id = fs.put(img)
    storeItem = {
      "itemName": request.form["itemName"],
      "imgId": img_id, 
      "buyPrice": request.form["buyPrice"],
    }
    inserted_item = insert_item_into_store(storeItem)
    return Response(
      response=json.dumps( # send object as a json
        {
          "message": "Store item succesfully added", 
          "itemName": f"{inserted_item['itemName']}",
          "imgId": f"{inserted_item['imgId']}",
          "buyPrice": f"{inserted_item['buyPrice']}",
        }
      ), 
      status=200, 
      mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(
      response=json.dumps( # send object as a json
        {
          "message": "Store item cannot be added", 
        }
      ), 
      status=500, 
      mimetype="application/json")

########################################
# To get all items in the store
@app.route("/store", methods=["GET"])
def get_all_store_items():
  try:
    store_items = list(db.store.find())
    for item in store_items: # convert object id to string since object id is not json serializable
      item["_id"] = str(item["_id"])
      item["imgId"] = str(item["imgId"])
    return Response(
      response=json.dumps(store_items), 
      status=200, 
      mimetype="application/json")
  except Exception as ex:
    print(ex)
    return Response(
      response=json.dumps( # send object as a json
        {
          "message": "Store items cannot be retrieved", 
        }
      ), 
      status=500, 
      mimetype="application/json")

########################################
# Run your flask app on port 80
if __name__ == "__main__":
  app.run(port=80, debug=True)