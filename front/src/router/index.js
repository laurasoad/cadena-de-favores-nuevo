import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('@/pages/about/AboutPage.vue'),
  },
  {
    path: '/publications',
    name: 'PublicationList',
    component: () => import('@/pages/publications-list/PublicationsListPage.vue'),
  },
  {
    path: "/publications/:id",
    name: "PublicationDetail",
    component: () => import('@/pages/publication-detail/PublicationDetailPage.vue'),
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
