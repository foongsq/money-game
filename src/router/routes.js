import Dashboard from '../views/Dashboard.vue';
import Authentication from '../views/Authentication.vue';
import AdminDashboard from '../views/AdminDashboard.vue';

const routes = [
  { path: '/authentication', component: Authentication },
  { path: '/', component: Dashboard },
  { path: '/admin-dashboard', component: AdminDashboard }
]

export default routes;