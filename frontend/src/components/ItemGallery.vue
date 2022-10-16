<template>
  <div class="outerDiv">
    <div :class="itemType == itemTypes.INVENTORY ? 'yellowInnerDiv' : 'purpleInnerDiv'">
      <div class="title"><h3>{{title}}</h3></div>
      <div class="cardGroup">
        <b-card
          v-for="(item, index) in items" 
          :key="index"
          title-tag="p"
          style="height: 100%; margin: 0 0.25rem; flex: 0 0 auto;"
        >
          <p style="maxWidth: 125px">{{item.itemName}}</p>
          <img :src="formatImage(item.base64Img)" height="125px" style="marginBottom: 0.25rem" />
          <div class="quantity" v-if="itemType == itemTypes.INVENTORY"><p><b>Quantity</b>:{{item.quantity}}</p></div>
          <div class="quantity" v-if="itemType == itemTypes.STORE && !isAdmin"><p>ON SALE!</p></div>
          <b-button v-if="isAdmin && itemType == itemTypes.STORE" size="sm" href="#" variant="primary" class="actionButton" style="font-size: 0.75rem;" @click="onDelete(item)">{{action}}</b-button>
          <b-button v-else size="sm" href="#" variant="primary" style="font-size: 0.75rem;" class="actionButton" @click="onAction(itemType, item)">{{action}} ${{item.price}}</b-button>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import { itemTypes } from '../constants'

export default {
  name: 'ItemGallery',
  props: {
    itemType: String,
    isAdmin: Boolean,
    title: String,
    items: Array,
    action: String,
  },
  data () {
    return {
      itemTypes: itemTypes,
    }
  },
  methods: {
    ...mapActions([
      'buyItem', 'sellItem', 'deleteItem'
    ]),
    formatImage (img) {
      return "data:image/jpg;base64, " + img;
    },
    async onAction (itemType, item) {
      if (itemType == itemTypes.INVENTORY) {
        await this.sellItem(item['store_item_id']);
      } else if (itemType == itemTypes.STORE) {
        await this.buyItem(item['_id']);
      } else {
        throw 'Wrong item type supplied'
      }
    },
   async onDelete (item) {
      await this.deleteItem(item['_id']);
    }
  },
}
</script>

<!-- Not scoped because we want AdminDashboard to receive same styling for store -->
<style>
.outerDiv {
  padding: 0.5rem;
  /* height: 40vh; */
}
/*  - Add margin and padding around inventory
    - add black rounded border
    - yellow background color 
    - max height is 40vh*/
.yellowInnerDiv {
  padding: 0.5rem;
  border: 1px solid black;
  border-radius: 10px;
  background: var(--light-yellow);
  height: 100%;
}

.purpleInnerDiv {
  padding: 0.5rem;
  border: 1px solid black;
  border-radius: 10px;
  background: var(--light-purple);
  height: 100%;
}

.title {
  height: 15%; 
  display: flex; 
  align-items: center; 
  justify-content: center;
}

.cardGroup {
  overflow-x: auto; 
  overflow-y: scroll; 
  display: flex; 
  flex-wrap: nowrap; 
}

.cardGroup::-webkit-scrollbar {
  display: none;
}

.quantity {
  background-color: var(--light-yellow);
  border-radius: 5px;
  padding: 0 0.25rem;
  font-size: 0.75rem;
  margin-top: 0.25rem;
}

.actionButton {
  width: 100%;
}
</style>
