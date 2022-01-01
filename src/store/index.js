import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

// Make Vuex globally available throughout the app
Vue.use(Vuex);

const store = new Vuex.Store({
  namespaced: false,
  // Data
  state: {
    username: null,
    money: null,
    inventory: [],
    store: [],
  },

  // Getters
  getters: {
    getUsername: state => state.username,
    getMoney: state => state.money,
    getInventory: state => state.inventory,
    getStore: state => state.store,
  },

  // Setters
  mutations: {
    setUsername: (state, username) => { state.username = username; },
    setMoney: (state, money) => { state.money = money; },
    setInventory: (state, inventory) => { state.inventory = inventory; },
    setStore: (state, store) => { state.store = store; },
  },

  // Methods called (dispatch) by Vue components, 
  // which interacts with backend api, 
  // and call setters (commit mutations)
  actions: {
    // async signup ({ dispatch }, payload) { 

    // },
    // async signin ({ commit }) { },
    // async signout ({ commit }) { },
    // async fetchUser ({ commit }) { },
    async fetchStore ({ commit }) { 
      // Fetch store items from api
      const store = await axios.get("/api/store").then(
        (response) => response.data, 
        (error) => { console.log(error);}
        );
      // Call setter to save fetched store items into store attribute in state
      commit('setStore', store);
    },
    // async work ({ commit, dispatch }) { },
    // async buyItem ({ commit, dispatch }) { },
    // async sellItem ({ commit, dispatch }) { },
    // async addItem ({ commit, dispatch }) { },
    // async deleteItem ({ commit, dispatch }) { },
  }
})

export default store;