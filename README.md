# Money Game

## Purpose of this game

The purpose of this simple game is to allow me to get familiar with api development and NoSQL database design.

## How the game works

Upon signing in to the game, users can press a button labelled `Work` to earn coins. Users can then use the coins they have earned to buy things from a store. Upon buying an item from the store, the item will be added into the user's inventory, where they can choose to sell the item for coins. 

The original motivation behind this game was crypto/NFT related. However, I wanted to keep the game as simple as possible so that I can focus on learning backend programming.

**Frontend mock ups:**

Note: This app was only designed to be used on mobile, not on desktop.

<p align="center">
  <img src="./docs/images/frontend_mvp_normal_mockup.png" alt="frontend mockup normal users" height="450px">
  <img src="./docs/images/frontend_mvp_admin_mockup.png" alt="frontend mockup admin" height="450px">
  <img src="./docs/images/frontend_mvp_auth_mockup.png" alt="frontend mockup authentication" height="450px">
</p>

**Database Schema:**
* **Authentication:** unique username and password to signin
* **Money**
* **Inventory:** itemid, picture, quantity, sell price
* **Store:** itemid, picture, buy price

<p align="center">
  <img src="./docs/images/database_plan.png" alt="database schema" height="400px">
</p>

**Abstract backend API used by normal users:**

- [x] `/user`: POST method that takes unique username, password, and creates a user in the database, returns userId
- [x] `/user`: POST method that username, password, returns userId
- [x] `/money`: POST/UPDATE method that takes userId, and updated money
- [x] `/inventory`: GET method that gets all items in inventory
- [x] `/store`: GET method that gets all items in store
- [x] `/inventoryItem`: POST/UPDATE method -> buy; decrement money; if item in inventory, increment quantity by 1; else, add item;
- [x] `/inventoryItem`: POST/UPDATE method -> sell; decrement quantity; increment money

**Abstract backend API used by admin:**
- [x] `/user`: POST method that username, password, returns userId of admin
- [x] `/store`: GET method that gets all items in store
- [x] `/storeItem`: POST method that uploads new item to store (picture, name, price, auto snag id)
- [x] `/storeItem` : DELETE method that deletes an item from store

**Backend features:**
- hashed passwords
- enforce unique usernames

## Vue Project setup
**Install dependencies:** `npm install`

**Compiles and hot-reloads for development:** `npm run serve`

**Compiles and minifies for production:** `npm run build`

**Lints and fixes files:** `npm run lint`

**Customize configuration:** See [Configuration Reference](https://cli.vuejs.org/config/).

## API Project setup
All sequences of commands are assumed to be run from the root directory.

**Activating python virtual environment:** 
```
cd api/Scripts
activate
```

**Install dependencies:** 
```
cd api
pip install -r requirements.txt
```

**Run server:** 
```
cd api/routes
python app.py
```

## Infrastructure
**Technological Stack:**
<p align="center">
  <img src="./docs/images/tech_stack.png" alt="tech stack" height="400px">
</p>

**Backend Infrastructure:**
<p align="center">
  <img src="./docs/images/backend_infra.png" alt="backend infrastructure" height="400px">
</p>

**Additional Libraries/Packages used:**
* [Vue 3D Carousel](https://github.com/wlada/vue-carousel-3d)
* [PyJWT](https://pyjwt.readthedocs.io/en/stable/usage.html)

**References:**
* [Handling file uploads in Vue](https://www.digitalocean.com/community/tutorials/how-to-handle-file-uploads-in-vue-2)
* [Flask and MongoDB tutorial](https://www.youtube.com/watch?v=o8jK5enu4L4)
* [API Development Course](https://www.youtube.com/watch?v=0sOvCWFmrtA)
* [Sending image files from backend to frontend](https://stackoverflow.com/questions/33279153/rest-api-file-ie-images-processing-best-practices)
* [base64 encode in python and decode in javascript](https://stackoverflow.com/questions/35443332/base64-encode-in-python-decode-in-javascript)
* [render base64 image in vue](https://stackoverflow.com/questions/46492356/render-base64-image-in-vue-js)
