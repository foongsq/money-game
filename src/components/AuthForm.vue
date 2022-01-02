<template>
  <div class="authForm">
    <h3>{{ text }}</h3>
    <b-form-input class="authInput" v-model="username" placeholder="Enter your username"></b-form-input>
    <b-form-input class="authInput" v-model="password" type="password" placeholder="Enter your password"></b-form-input>
    <b-button class="authButton" variant="light">{{ text }}</b-button>
  </div>
</template>

<script>
export default {
  name: 'AuthForm',
  props: {
    authType: String,
    text: String,
  },
  data() {
    return {
      username: '',
      password: '',
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
.authForm {
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
