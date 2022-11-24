import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import LoginView from '@/views/LoginView'
import ProfileView from '@/views/ProfileView'
import RecommendView from '@/views/RecommendView'
import SearchView from '@/views/SearchView'
import SignUpView from '@/views/SignUpView'
import MovieDetailView from '@/views/MovieDetailView'
import ReviewDetailView from '@/views/ReviewDetailView'
import FollowerListView from '@/views/FollowerListView'
import FollowingListView from '@/views/FollowingListView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: RecommendView,
  },
  {
    path: '/search/:userinput',
    name: 'search',
    component: SearchView,
  },
  {
    path: '/movie/:id',
    name: 'movie',
    component: MovieDetailView,
  },
  {
    path: '/profile/:id',
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/profile/:id/followerlist',
    name: 'followerlist',
    component: FollowerListView
  },
  {
    path: '/profile/:id/followinglist',
    name: 'followinglist',
    component: FollowingListView
  },
  {
    path: '/review/:id',
    name: 'review',
    component: ReviewDetailView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
