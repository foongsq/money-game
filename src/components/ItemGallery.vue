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
          style="font-size: 0.75rem; height: 100%; margin: 0 0.25rem; border: 1px solid blue; flex: 0 0 auto;"
        >
          <b-button size="sm" href="#" variant="primary" style="font-size: 0.75rem;">{{action}} ${{item.price}}</b-button>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
import { itemTypes } from '../constants'

export default {
  name: 'ItemGallery',
  components: {

  },
  props: {
    itemType: String,
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
    formatImage (img) {
      return "data:image/jpg;base64, " + img;
    }
  },
  created: function() {
    console.log(itemTypes.INVENTORY)
  }
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
</style>
