<template>
  <div class="workButtonDiv">
    <button class="btn btn-success w-100" @click="onWork(money)">Work (+10)</button>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'WorkButton',
  computed: {
    ...mapGetters({
      money: 'getMoney',
    }),
  },
  methods: {
    ...mapActions([
      'work'
    ]),
    onWork(money) {
      //TODO: Optimize later
      let moneyValue = parseFloat(money);
      moneyValue += 10.0;
      this.work(moneyValue);
    },
  },
}
</script>

<!-- Not scoped because we want AdminDashboard to receive same styling for store -->
<style>
/* Add padding and margin to buttons */
.workButtonDiv {
  height: 7.5vh;
  padding: 0.25rem;
  display: flex;
}
</style>
