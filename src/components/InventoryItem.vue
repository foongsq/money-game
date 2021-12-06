<template>
  <button class="inventoryItemButton">
    <div class="inventoryItem">
      <img class="itemImg" :src='"../assets/chips.jpg"' height="400" width="400"/>
      <p class="itemName">{{itemName}}</p>
      <p class="quantity">{{quantity}}</p>
    </div>
    <div class="sellPriceButton">
      <p>Sell for</p>
      <img class="moneyImage" :src='"../assets/money-icon.jpg"' />
      <p>{{sellPrice ? sellPrice : 3}}</p>
    </div>
  </button>
</template>

<script>
export default {
  name: 'InventoryItem',
  props: {
    itemId: Number,
    imgUrl: String,
    itemName: String,
    sellPrice: Number,
    quantity: Number,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.inventoryItemButton {
  height: 100%;
  width: 100%;
  border: none;
  background: transparent;
}

.inventoryItemButton:hover > .inventoryItem {
  display: none;
}
/* Make store item component take up 100% of carousel's height,
  add padding, flex components within it vertically */
.inventoryItem {
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
  margin: 0.5rem 0 0 0;
}

/* Hardcode position of quantity label */
.quantity {
  background: orange;
  font-size: 0.75rem;
  padding: 0.25rem;
  border-radius: 50%;
  position: absolute;
  left: 5%;
  top: 5%;
}

/* Make coin image round and set max height/width */
.moneyImage {
  border-radius: 50%;
  max-height: 30px;
  max-width: 30px;
}

/* flex the components within button and center them vertically,
  then set background color to purple. Remove border, and round the button,
  finally set padding and center button horizontally */
.sellPriceButton {
  display: flex;
  justify-content: center;
  align-items: center;
  background: transparent;
  border: none;
  border-radius: 5px;
  padding: 0 0.5rem;
  margin: 0 auto;
}

/* Add space between words and coin icon in button */
.sellPriceButton p {
  margin: 0.5rem;
}
</style>
