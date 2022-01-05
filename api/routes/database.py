import pymongo # To connect flask app to mongodb
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_PASS = os.getenv('MONGODB_PASS')
DB_NAME = "moneygame-db"

# Connect to mongodb (always wrap connection in try except block)
try:
  mongo = pymongo.MongoClient(f"mongodb+srv://moneygame-admin:{MONGODB_PASS}@moneygame-db.2gc9y.mongodb.net/{DB_NAME}?retryWrites=true&w=majority")
  db = mongo.test # access database named moneygame
  mongo.server_info() # trigger exception if connection fails
except Exception as e: 
  print('Error connecting to MongoDB')
  print(e)