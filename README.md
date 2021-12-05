# Money Game

## Minimum Viable Product

**Technological Stack:**
<p align="center">
  <img src="./docs/images/tech_stack.png" alt="tech stack" height="400px">
</p>

**Frontend mock ups:**
<p align="center">
  <img src="./docs/images/frontend_mvp_normal_mockup.png" alt="frontend mockup normal users" height="450px">
  <img src="./docs/images/frontend_mvp_admin_mockup.png" alt="frontend mockup admin" height="450px">
  <img src="./docs/images/frontend_mvp_auth_mockup.png" alt="frontend mockup authentication" height="450px">
</p>

**Data:**
* unique user name to login
* money,
* inventory: itemid, picture, quantity, sell price
* store: itemid, picture, buy price

**Backend endpoints used by normal users:**
* create account (unique username, password)
* login (username, password)
* addMoney
* buyItem (if item in inventory, incrememnt quantity by 1, if not, add item, decrement money)
* sellItem (decrement quantity, incrememnt money)

**Backend endpoints used by admin:**
* login
* addItem (picture, name, price, auto snag id): upload new item to store




## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
