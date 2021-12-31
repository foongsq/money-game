export default {
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
    async signup () { },
    async signin () { },
    async signout () { },
    async fetchUser () { },
    async fetchStore () { },
    async work () { },
    async buyItem () { },
    async sellItem () { },
    async addItem () { },
    async deleteItem () { },
  }
}