<template>
  <div class="spinner">
    <b-spinner variant="secondary"></b-spinner>
  </div>
</template>

<script>
export default {
  name: 'Spinner',
}
</script>

<!-- Not scoped because we want AdminDashboard to receive same styling for store -->
<style>
.spinner {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
