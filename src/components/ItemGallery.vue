<template>
  <div class="outerDiv">
    <div :class="itemType == itemTypes.INVENTORY ? 'yellowInnerDiv' : 'purpleInnerDiv'">
      <div class="title"><h3>{{title}}</h3></div>
      <div class="cardGroup">
        <b-card
          v-for="(item, index) in items" 
          :title="item.itemName"
          :key="index"
          title-tag="p"
          :img-src="formatImage(item.base64Img)"
          img-alt="Image"
          img-height="50%"
          img-top
          style="height: 100%; margin: 0 0.25rem; flex: 0 0 auto;"
        >
          <div class="quantity" v-if="itemType == itemTypes.INVENTORY"><p><b>Quantity</b>:{{item.quantity}}</p></div>
          <b-button v-if="isAdmin && itemType == itemTypes.STORE" size="sm" href="#" variant="primary" style="font-size: 0.75rem;" @click="onDelete(item)">{{action}}</b-button>
          <b-button v-else size="sm" href="#" variant="primary" style="font-size: 0.75rem;" @click="onAction(itemType, item)">{{action}} ${{item.price}}</b-button>
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
  height: 40vh;
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
  overflow-y: hidden; 
  display: flex; 
  flex-wrap: nowrap; 
  height: 83%;
}

.quantity {
  background-color: var(--light-yellow);
  border-radius: 5px;
  padding: 0 0.25rem;
  font-size: 0.75rem;
}
</style>
