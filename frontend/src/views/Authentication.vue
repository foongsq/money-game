<template>
  <div class="authentication">
    <h1>Welcome!</h1>
    <AuthForm :authType="authTypes.SIGNIN" text="Sign In"/>
    <AuthForm :authType="authTypes.SIGNUP" text="Sign Up"/>
  </div>
</template>

<script>
import AuthForm from '../components/AuthForm.vue'
import { authTypes } from '../constants'
import { pathNames } from '../router/routes'

export default {
  components: { AuthForm },
  name: 'Authentication',
  data() {
    return {
      authTypes: authTypes,
    }
  },
  created: function () {
    if (this.$store.state.username != null &&
        this.$store.state.username != 'admin') {
      this.$router.push(pathNames.DASHBOARD);
    } else if (this.$store.state.username != null &&
      this.$store.state.username == 'admin') {
      this.$router.push(pathNames.ADMINDASHBOARD);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.authentication {
  max-width: 600px;
  height: 100vh;
  padding: 1rem 0;
}
</style>
