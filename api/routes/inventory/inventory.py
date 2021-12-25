
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