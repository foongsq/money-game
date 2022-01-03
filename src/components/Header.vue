<template>
  <div class="userParticularsDiv">
    <div class="userNameDiv"><p>{{ username }}</p></div>
    <Money />
  </div>
</template>

<script>
import Money from './Money.vue';

export default {
  name: 'Header',
  components: {
    Money
  },
  props: {
    username: String,
  },
  data: function () {
    return {

    }
  },
  methods: {
   
  },
  created: function() {
  
  }
}
</script>

<!-- Not scoped because we want AdminDashboard to receive same styling for store -->
<style>
.userParticularsDiv {
  display: flex;
  justify-content: space-between;
  height: 5vh;
  padding-top: 0.5rem;
}

/* Need to flex in order to be able to center vertically using margin */
.userNameDiv {
  display: flex;
  margin: 0 1rem;
}

/* To center the money value vertically */
.userNameDiv p {
  margin: auto 0;
  padding: 0;
}

/* To put money icon and money value side by side */
.moneyDiv {
  display: flex;
  align-items: center;
  margin: 0 1rem;
}

.moneyIcon {
  max-height: 100%;
  max-width: 100%;
  display: block;
  height: auto;
  width: auto;
}

/* To center the money value vertically */
.moneyDiv p {
  margin: auto 0.5rem;
}
</style>
