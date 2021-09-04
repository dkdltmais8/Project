import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import MyPage from '../views/MyPage.vue'
import Community from '../views/Community.vue'
import WriteReview from '../components/WriteReview.vue'
import UpdateReview from '../components/UpdateReview.vue'
import ReviewDetail from '../components/ReviewDetail'
import SignUp from '../components/SignUp.vue'
import Login from '../components/Login.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/myPage',
    name: 'MyPage',
    component: MyPage
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/community/write-review',
    name: 'WriteReview',
    component: WriteReview
  },
  {
    path: '/community/:review_pk',
    name: 'ReviewDetail',
    component: ReviewDetail,
  },
  {
    path: '/community/:review_pk/update',
    name: 'UpdateReview',
    component: UpdateReview,
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
