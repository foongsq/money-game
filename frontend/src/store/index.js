import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

// Make Vuex globally available throughout the app
Vue.use(Vuex);

const API_URL = process.env.BACKEND_URL;

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
    getUsername: (state) => state.username,
    getMoney: (state) => state.money,
    getInventory: (state) => state.inventory.reverse(),
    getStore: (state) => state.store.reverse(),
  },

  // Setters
  mutations: {
    setUsername: (state, username) => {
      state.username = username;
    },
    setMoney: (state, money) => {
      state.money = money;
    },
    setInventory: (state, inventory) => {
      state.inventory = inventory;
    },
    setStore: (state, store) => {
      state.store = store;
    },
  },

  // Methods called (dispatch) by Vue components,
  // which interacts with backend api,
  // and call setters (commit mutations)
  actions: {
    async signup({ dispatch }, payload) {
      const formData = new FormData();
      formData.append("username", payload.username);
      formData.append("password", payload.password);

      await axios
        .post(API_URL + "/api/user", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then(
          (response) => response.data,
          (error) => {
            console.log(error);
          }
        );

      dispatch("signin", payload);
    },
    async signin({ dispatch }, payload) {
      const formData = new FormData();
      formData.append("username", payload.username);
      formData.append("password", payload.password);

      try {
        const res = await axios.post(API_URL + "/api/session", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        console.log(res.data.token);
        window.localStorage.setItem("token", res.data.token);
      } catch (e) {
        console.error(e);
      }
      dispatch("fetchUser");
    },

    async signout({ commit }) {
      window.localStorage.setItem("token", null);
      commit("setUsername", null);
      commit("setMoney", null);
      commit("setInventory", []);
    },

    async fetchUser({ commit }) {
      const response = await axios
        .get(API_URL + "/api/session", {
          withCredentials: true,
          headers: {
            "x-access-token": window.localStorage.getItem("token"),
          },
        })
        .then(
          (response) => response.data.data,
          (error) => {
            throw error.response;
          }
        );
      commit("setUsername", response.username);
      commit("setMoney", response.money);
      commit("setInventory", response.inventory);
    },

    async fetchStore({ commit }) {
      // Fetch store items from api
      const store = await axios.get(API_URL + "/api/store").then(
        (response) => response.data,
        (error) => {
          console.log(error);
        }
      );
      // Call setter to save fetched store items into store attribute in state
      commit("setStore", store);
    },

    async work({ commit }, money) {
      const formData = new FormData();
      formData.append("money", money);

      const response = await axios
        .post(API_URL + "/api/money", formData, {
          withCredentials: true,
          headers: {
            "Content-Type": "multipart/form-data",
            "x-access-token": window.localStorage.getItem("token"),
          },
        })
        .then(
          (response) => response.data,
          (error) => {
            console.log(error);
          }
        );
      commit("setMoney", response.money);
    },

    async buyItem({ commit }, itemId) {
      const formData = new FormData();
      formData.append("action", "buy");
      formData.append("itemId", itemId);

      const response = await axios
        .post(API_URL + "/api/inventoryItem", formData, {
          withCredentials: true,
          headers: {
            "Content-Type": "multipart/form-data",
            "x-access-token": window.localStorage.getItem("token"),
          },
        })
        .then(
          (response) => response.data,
          (error) => {
            console.log(error);
          }
        );
      commit("setMoney", response.money);
      commit("setInventory", response.inventory);
    },

    async sellItem({ commit }, itemId) {
      const formData = new FormData();
      formData.append("action", "sell");
      formData.append("itemId", itemId);

      const response = await axios
        .post(API_URL + "/api/inventoryItem", formData, {
          withCredentials: true,
          headers: {
            "Content-Type": "multipart/form-data",
            "x-access-token": window.localStorage.getItem("token"),
          },
        })
        .then(
          (response) => response.data,
          (error) => {
            console.log(error);
          }
        );
      commit("setMoney", response.money);
      commit("setInventory", response.inventory);
    },
    async addItem({ dispatch }, newStoreItem) {
      const formData = new FormData();
      formData.append("img", newStoreItem.newItemImageFile);
      formData.append("itemName", newStoreItem.newItemName);
      formData.append("price", newStoreItem.newItemPrice);

      await axios
        .post(API_URL + "/api/storeItem", formData, {
          withCredentials: true,
          headers: {
            "Content-Type": "multipart/form-data",
            "x-access-token": window.localStorage.getItem("token"),
          },
        })
        .then(
          (response) => response.data,
          (error) => {
            console.log(error);
          }
        );

      dispatch("fetchStore");
    },
    async deleteItem({ dispatch }, itemId) {
      const url = API_URL + "/api/storeItem/" + itemId;
      await axios
        .delete(url, {
          withCredentials: true,
          headers: {
            "x-access-token": window.localStorage.getItem("token"),
          },
        })
        .then(
          (response) => response.data,
          (error) => {
            throw error.response;
          }
        );

      dispatch("fetchStore");
    },
  },
});

export default store;
