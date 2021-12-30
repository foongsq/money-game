import Vue from 'vue'
import VueRouter from 'vue-router'
import routes from './routes'

// Make VueRouter available globally
Vue.use(VueRouter)

const router = new VueRouter({
  routes, // short for `routes: routes`
  mode: 'history' // history mode vs hash mode, history allows use to use pushState to navigate around without reloading page
})

export default router;