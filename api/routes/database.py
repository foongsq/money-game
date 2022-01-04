import pymongo # To connect flask app to mongodb
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_PASS = os.getenv('MONGODB_PASS')

# Connect to mongodb (always wrap connection in try except block)
try:
  mongo = pymongo.MongoClient(
    host=f"mongodb+srv://moneygame-admin:{MONGODB_PASS}@moneygame-db.2gc9y.mongodb.net/moneygameDB?retryWrites=true&w=majority", 
    port=27017, # default TCP port used by mongodb
    serverSelectionTimeoutMS=1000 # if cannot connect in 1000ms, means connection failed
  )
  db = mongo.moneygame # access database named moneygame
  mongo.server_info() # trigger exception if connection fails
except: 
  print("Error - Cannot connect to db")