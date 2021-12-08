from flask import Flask, Response, request
import pymongo # To connect flask app to mongodb
import json
from bson.objectid import ObjectId

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
  mongo.server_info() # trigger exception if connection fails
except: 
  print("Error - Cannot connect to db")

########################################
# To add a new user (with username, password, and 0 money, 
# and empty inventory) into the database
# TODO: Make sure username is not already in the database
@app.route("/signup", methods=["POST"])
def signup():
  try:
    user = {
      "username": request.form["username"], 
      "password": request.form["password"],
      "money": 0,
      "inventory": [],
    }
    dbResponse = db.users.insert_one(user)
    return Response(
      response=json.dumps( # send object as a json
        {
          "message": "User created successfully", 
          "id":f"{dbResponse.inserted_id}"
        }
      ), 
      status=200, 
      mimetype="application/json")
  except Exception as ex:
    print(ex)

########################################
# To get all user's data from the database
@app.route("/signin", methods=["GET"])
def signin():
  try:
    data = list(db.users.find({"username": request.form["username"]}))
    return Response(
      response=json.dumps( # send object as a json
        {
          "message": "User succesfully retrieved", 
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
# To get a userid from the database
@app.route("/addMoney", methods=["POST"])
def addMoney():
  try:
    dbResponse = db.users.update_one(
      {"username": request.form["username"]},
      {"$set": { "money": request.form["money"]}}
    )
    # for attr in dir(dbResponse):
    #   print(attr)
    return Response(
      response=json.dumps( # send object as a json
        {
          "message": "Money succesfully updated", 
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
# Run your flask app on port 80
if __name__ == "__main__":
  app.run(port=80, debug=True)