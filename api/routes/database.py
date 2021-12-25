import pymongo # To connect flask app to mongodb

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