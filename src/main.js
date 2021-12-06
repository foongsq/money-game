import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Dashboard from './views/Dashboard.vue';
import Authentication from './views/Authentication.vue';
// import AdminDashboard from './views/AdminDashboard.vue';


// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
// Make VueRouter available globally
Vue.use(VueRouter)

Vue.config.productionTip = false

const routes = [
  { path: '/authentication', component: Authentication },
  { path: '/', component: Dashboard },
  // { path: '/admin-dashboard', component: AdminDashboard }
]

const router = new VueRouter({
  routes // short for `routes: routes`
})

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
