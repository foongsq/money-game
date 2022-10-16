from database import db

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