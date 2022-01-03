<template>
  <div class="moneyDiv">
    <img className="moneyIcon" src="../assets/money-icon.jpg" height="20px"/>
    <p>{{ money }}</p>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'Money',
  computed: {
    ...mapGetters({
      money: 'getMoney',
    }),
  },
  data: function () {
    return {

    }
  },
  methods: {
    ...mapActions([
      'fetchUser',
    ]),
  },
  created: async function() {
    await this.fetchUser();
  }
}
</script>

<!-- Not scoped because we want AdminDashboard to receive same styling for store -->
<style>
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
