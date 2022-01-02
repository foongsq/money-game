<template>
  <div class="workButtonDiv">
    <button class="btn btn-success w-100" @click="onWork">Work (+10)</button>
  </div>
</template>

<script>
export default {
  name: 'WorkButton',
  methods: {
    onWork() {
      this.myMoney += 10;
    },
  },
}
</script>

<!-- Not scoped because we want AdminDashboard to receive same styling for store -->
<style>
/* Add padding and margin to buttons */
.workButtonDiv {
  height: 7.5vh;
  border: 1px solid red;
  padding: 0.25rem;
  display: flex;
}
</style>
