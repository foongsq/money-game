import Dashboard from '../views/Dashboard.vue';
import Authentication from '../views/Authentication.vue';
import AdminDashboard from '../views/AdminDashboard.vue';

export const pathNames = {
  "DASHBOARD": "/dashboard",
  "AUTHENTICATION": "/auth",
  "ADMINDASHBOARD": "/admin",
};

const routes = [
  { path: '/', redirect: '/dashboard' },
  { path: '/dashboard', component: Dashboard },
  { path: '/auth', component: Authentication },
  { path: '/admin', component: AdminDashboard }
]

export default routes;