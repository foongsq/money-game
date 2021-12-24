<template>
  <button class="storeItemButton">
    <div class="storeItem">
      <img class="itemImg" :src='img_formatted' height="400" width="400"/>
      <p class="itemName">{{itemName}}</p>
    </div>
    <div v-if="isAdmin" class="buyPriceButton">
      <p>Delete</p>
    </div>
    <div v-else class="buyPriceButton">
      <p>Buy for</p>
      <img class="moneyImage" :src='"../assets/money-icon.jpg"' />
      <p>{{buyPrice ? buyPrice : 3}}</p>
    </div>
  </button>
</template>

<script>
export default {
  name: 'StoreItem',
  props: {
    img: String,
    itemName: String,
    buyPrice: String,
    isAdmin: Boolean,
  },
  computed: {
    img_formatted: function () {
      return "data:image/jpg;base64, " + this.img;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.storeItemButton {
  height: 100%;
  width: 100%;
  border: none;
  background: transparent;
}

.storeItemButton:hover > .storeItem {
  display: none;
}
/* Make store item component take up 100% of carousel's height,
  add padding, flex components within it vertically */
.storeItem {
  height: 100%;
  padding: 0.5rem 0;
  display: flex;
  flex-direction: column;
}

/* Make item image take up 65% of the carousel card,
  and center the image */
.itemImg {
  max-height: 80%;
  max-width: 100%;
  margin: 0 auto;
  border-radius: 5px;
  display: block;
  height: auto;
  width: auto;
}

/* Center the item name, and add margin */
.itemName {
  text-align: center;
  margin: 0.5rem 0;
}

/* Make coin image round and set max height/width */
.moneyImage {
  border-radius: 50%;
  max-height: 20px;
  max-width: 20px;
}

/* flex the components within button and center them vertically,
  then set background color to purple. Remove border, and round the button,
  finally set padding and center button horizontally */
.buyPriceButton {
  display: flex;
  justify-content: center;
  align-items: center;
  background: transparent;
  border: none;
  border-radius: 5px;
  margin: 0 auto;
}

/* Add space between words and coin icon in button */
.buyPriceButton p {
  margin: 0.5rem;
}
</style>
