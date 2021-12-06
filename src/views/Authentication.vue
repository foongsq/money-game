<template>
  <div class="authentication">
    <h1>Welcome!</h1>
    <div class="signin">
      <h3>Sign In</h3>
      <b-form-input class="authInput" v-model="signinUsername" placeholder="Enter your username"></b-form-input>
      <b-form-input class="authInput" v-model="signinPassword" type="password" placeholder="Enter your password"></b-form-input>
      <b-button class="authButton" variant="light" >Sign In</b-button>
    </div>
    <div class="signup">
      <h3>Sign Up</h3>
      <b-form-input class="authInput" v-model="signupUsername" placeholder="Enter an unique username"></b-form-input>
      <b-form-input class="authInput" v-model="signupPassword" type="password" placeholder="Enter your password"></b-form-input>
      <b-button class="authButton" variant="light">Sign Up</b-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Authentication',
  data() {
    return {
      signinUsername: '',
      signinPassword: '',
      signupUsername: '',
      signupPassword: '',
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.authentication {
  max-width: 600px;
  height: 100vh;
  padding: 1rem 0;
}

/* Round corner of border, change background color, 
add padding and margin, and white font */
.signin, .signup {
  border: 1px solid grey;
  border-radius: 10px;
  margin: 1rem 0.5rem;
  padding: 0.5rem;
  background: var(--slate-grey);
  color: white;
}

.authInput {
  margin: 1rem 0;
}

.authButton {
  margin-bottom: 1rem;
}
</style>
