<template>
  <div class="logoutButtonDiv">
    <button class="btn btn-secondary w-100" @click="onSignout">Logout</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'LogoutButton',
  methods: {
    ...mapActions([
      'signout'
    ]),
    onSignout () {
      this.signout();
      this.$router.push('/authentication');
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
