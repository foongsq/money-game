<template>
  <div class="dashboard">
    <Header :username="username" :money="money"/>
    <ItemGallery :itemType="itemTypes.INVENTORY" title="My Inventory" :items="myInventory" action="Sell"/>
    <ItemGallery :itemType="itemTypes.STORE" title="Store" :items="store" action="Buy"/>
    <WorkButton />
    <LogoutButton />
    </div>
</template>

<script>
import { mapActions } from 'vuex'
import { itemTypes } from '../constants'
import ItemGallery from '../components/ItemGallery.vue'
import Header from '../components/Header.vue'
import WorkButton from '../components/WorkButton.vue'
import LogoutButton from '../components/LogoutButton.vue'

export default {
  name: 'Dashboard',
  components: {
    Header, ItemGallery, WorkButton, LogoutButton,
  },
  computed: {
    store: {
      get () {
        return this.$store.getters.getStore;
      },
      set (newStore){ // need to include this in order to use v-for in carousel but this should not be called, because store data shouldnt be overriden
        return newStore
      } 
    },
  },
  data: function () {
    return {
      itemTypes: itemTypes,
      username: "user321",
      money: 550,
      myInventory: [
        {itemId: 0, imgUrl: "../assets/chips.jpg", itemName: "chips1", price: 3, quantity: 1},
        {itemId: 1,imgUrl: "../assets/chips.jpg",itemName: "chips2",price: 30,quantity: 1000,},
        {itemId: 2,imgUrl: "../assets/chips.jpg",itemName: "chips3",price: 300,quantity: 11,},
        {itemId: 3,imgUrl: "../assets/chips.jpg",itemName: "chipolata",price: 13,quantity: 10,},
      ],
    }
  },
  methods: {
    ...mapActions([
      'fetchStore' // map `this.fetchStore()` to `this.$store.dispatch('fetchStore')`
    ]),
    formatImage (img) {
      return "data:image/jpg;base64, " + img;
    }
  },
  created: async function() {
    await this.fetchStore();
  }
}
</script>

<!-- Not scoped because we want AdminDashboard to receive same styling for store -->
<style>
.dashboard {
  max-width: 600px;
  height: 100vh;
}
</style>
