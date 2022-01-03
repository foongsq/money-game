<template>
  <div class="logoutButtonDiv">
    <button class="btn btn-secondary w-100" @click="onSignout">Logout</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import { pathNames } from '../router/routes'

export default {
  name: 'LogoutButton',
  methods: {
    ...mapActions([
      'signout'
    ]),
    onSignout () {
      this.$router.push(pathNames.AUTHENTICATION);
      this.signout();
    }
  },
}
</script>

<!-- Not scoped because we want AdminDashboard to receive same styling for store -->
<style>
/* Add padding and margin to buttons */
.logoutButtonDiv {
  height: 7.5vh;
  padding: 0.25rem;
  display: flex;
}

.logoutLink {
  text-decoration: none;
}
</style>
