# Money Game

## Minimum Viable Product
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

**Backend endpoints used by normal users:**
* `signup` (unique username, password)
* `signin` (username, password)
* `addMoney`
* `buyItem` (if item in inventory, incrememnt quantity by 1, if not, add item, decrement money)
* `sellItem` (decrement quantity, incrememnt money)

**Backend endpoints used by admin:**
* `signin`
* `addItem` (picture, name, price, auto snag id): upload new item to store
* `deleteItem` : delete item from store

## Project setup
**Install dependencies:** `npm install`

**Compiles and hot-reloads for development:** `npm run serve`

**Compiles and minifies for production:** `npm run build`

**Lints and fixes files:** `npm run lint`

**Customize configuration:** See [Configuration Reference](https://cli.vuejs.org/config/).

## Infrastructure
**Technological Stack:**
<p align="center">
  <img src="./docs/images/tech_stack.png" alt="tech stack" height="400px">
</p>

**Additional Libraries/Packages used:**
* [Vue 3D Carousel](https://github.com/wlada/vue-carousel-3d)
