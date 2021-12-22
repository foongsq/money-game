# Money Game

## Minimum Viable Product
This app was only designed to be used on mobile, not on desktop.

**Frontend mock ups:**
<p align="center">
  <img src="./docs/images/frontend_mvp_normal_mockup.png" alt="frontend mockup normal users" height="450px">
  <img src="./docs/images/frontend_mvp_admin_mockup.png" alt="frontend mockup admin" height="450px">
  <img src="./docs/images/frontend_mvp_auth_mockup.png" alt="frontend mockup authentication" height="450px">
</p>

**Data:**
* Authentication: unique username and password to signin
* Money
* Inventory: itemid, picture, quantity, sell price
* Store: itemid, picture, buy price

<p align="center">
  <img src="./docs/images/database_plan.png" alt="frontend mockup normal users" height="400px">
</p>

**Backend endpoints used by normal users:**
* `/signup`: POST method that takes unique username, password, and creates a user in the database, returns userId
* `/signin`: POST method that username, password, returns userId
* `/addMoney`: POST/UPDATE method that takes userId, and updated money
* `/getInventoryItems`: GET method that gets all items in inventory
* `/getStoreItems`: GET method that gets all items in store
* `/buyItem`: POST/UPDATE method -> decrement money; if item in inventory, incrememnt quantity by 1; else, add item;
* `/sellItem`: POST/UPDATE method -> decrement quantity; incrememnt money

**Backend endpoints used by admin:**
* `/signin`: POST method that username, password, returns userId of admin
* `/getStoreItems`: GET method that gets all items in store
* `/addStoreItem`: POST method that uploads new item to store (picture, name, price, auto snag id)
* `/deleteStoreItem` : DELETE method that deletes an item from store

## Vue Project setup
**Install dependencies:** `npm install`

**Compiles and hot-reloads for development:** `npm run serve`

**Compiles and minifies for production:** `npm run build`

**Lints and fixes files:** `npm run lint`

**Customize configuration:** See [Configuration Reference](https://cli.vuejs.org/config/).

## API Project setup
**Activating python virtual environment:** `cd api/Scripts`, `activate`

**Install dependencies:** `pip install flask pymongo`

**Run server:** `python server.py`

Open Postman to send requests

Open MongoDB Compass to look at database contents

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

**Tutorials referred to:**
* [Handling file uploads in Vue](https://www.digitalocean.com/community/tutorials/how-to-handle-file-uploads-in-vue-2)
* [Flask and MongoDB tutorial](https://www.youtube.com/watch?v=o8jK5enu4L4)
