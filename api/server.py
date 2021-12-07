from flask import Flask, Response, request
import pymongo # To connect flask app to mongodb
import json

# Create a flask app
app = Flask(__name__)

# Connect to mongodb (always wrap connection in try except block)
try:
  mongo = pymongo.MongoClient(
    host="localhost", 
    port=27017, # default TCP port used by mongodb
    serverSelectionTimeoutMS=1000 # if cannot connect in 1000ms, means connection failed
  )
  db = mongo.moneygame #create database named moneygame
  mongo.server_info() #trigger exception if connection fails
except: 
  print("Error - Cannot connect to db")

########################################
# To add a new user into the database
@app.route("/signup", methods=["POST"])
def signup():
  try:
    user = {
      "username": request.form["username"], 
      "password": request.form["password"],
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
# Run your flask app on port 80
if __name__ == "__main__":
  app.run(port=80, debug=True)