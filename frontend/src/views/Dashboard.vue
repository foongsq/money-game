<template>
  <div class="dashboard">
    <Spinner v-if="isLoading"/>
    <div v-else>
      <Header :username="username" :money="money"/>
      <ItemGallery :itemType="itemTypes.INVENTORY" title="My Inventory" :items="inventory" action="Sell"/>
      <ItemGallery :itemType="itemTypes.STORE" title="Store" :items="store" action="Buy"/>
      <WorkButton />
      <LogoutButton />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { itemTypes } from '../constants'
import ItemGallery from '../components/ItemGallery.vue'
import Header from '../components/Header.vue'
import WorkButton from '../components/WorkButton.vue'
import LogoutButton from '../components/LogoutButton.vue'
import { pathNames } from '../router/routes'
import Spinner from '../components/Spinner.vue'

export default {
  name: 'Dashboard',
  components: {
    Header, ItemGallery, WorkButton, LogoutButton,
    Spinner,
  },
  computed: {
    ...mapGetters({
      username: 'getUsername',
      money: 'getMoney',
      inventory: 'getInventory',
      store: 'getStore',
    }),
  },
  data: function () {
    return {
      itemTypes: itemTypes,
      isLoading: false,
    }
  },
  methods: {
    ...mapActions([
      'fetchStore', 'fetchUser',
    ]),
    formatImage (img) {
      return "data:image/jpg;base64, " + img;
    }
  },
  created: async function() {
    this.isLoading = true;
    await this.fetchStore();
    try {
      await this.fetchUser();
    } catch (e) {
      console.log(e);
      if (e.status == 401) {
        this.$router.push(pathNames.AUTHENTICATION)
      }
    }
    this.isLoading = false;
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
