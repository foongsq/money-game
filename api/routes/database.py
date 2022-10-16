import pymongo # To connect flask app to mongodb
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')
DB_NAME = "moneygame-db"

# Connect to mongodb (always wrap connection in try except block)
try:
  mongo = pymongo.MongoClient(MONGODB_URI)
  db = mongo.moneygame # access database named moneygame
  mongo.server_info() # trigger exception if connection fails
except: 
  print("Error - Cannot connect to db") 