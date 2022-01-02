<template>
  <div class="adminDashboard">
    <h1>Welcome Admin!</h1>
    <ItemForm />
    <ItemGallery :itemType="itemTypes.STORE" title="Store" :items="store" action="Buy"/>
    <div class="logoutButtonDiv">
      <button class="btn btn-secondary w-100">
        <router-link style="text-decoration: none; color: inherit;" to="/authentication">Logout</router-link>
      </button>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import ItemForm from '../components/ItemForm.vue';
import ItemGallery from '../components/ItemGallery.vue';

import { itemTypes } from '../constants'

export default {
  name: 'AdminDashboard',
  components: {
    ItemGallery,
    ItemForm
  },
  computed: {
    store: function () {
      return this.$store.getters.getStore;
    },
  },
  data: function() {
    return {
      itemTypes: itemTypes,
    }
  },
  methods: {
    ...mapActions([
      'fetchStore' // map `this.fetchStore()` to `this.$store.dispatch('fetchStore')`
    ]),
  },
  created: async function() {
    await this.fetchStore();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.adminDashboard {
  max-width: 600px;
  height: 100vh;
  padding: 1rem 0;
}
</style>
