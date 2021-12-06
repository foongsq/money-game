<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>

export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  box-sizing: border-box;
  --lighter-yellow: #ffecb5;
  --light-yellow: #ffe599;
  --light-medium-yellow: #e3ab00;
  --medium-yellow: #bf9000;
  --lighter-purple: #c8bfdd;
  --light-purple: #b4a7d6;
  --light-medium-purple: #a893e7;
  --medium-purple: #8e7cc3;
  --slate-grey: #6c757d;
}
</style>
