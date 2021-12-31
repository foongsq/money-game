import Vue from 'vue';
import Vuex from 'vuex';
import store from "./store.js";

// Make Vuex globally available throughout the app
Vue.use(Vuex);

export default new Vuex.Store({
  store,
})