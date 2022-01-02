<template>
  <div class="logoutButtonDiv">
    <button class="btn btn-secondary w-100">
      <router-link style="text-decoration: none; color: inherit;" to="/authentication" >Logout</router-link>
    </button>
  </div>
</template>

<script>
export default {
  name: 'LogoutButton',
  methods: {
    
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
