import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Index from '@/components/Index'
import Login from '@/components/Login'
import Register from '@/components/Register'
import ContestList from '@/components/contest/ContestList'
import ContestCreate from '@/components/contest/ContestCreate'
import ContestDetail from '@/components/contest/ContestDetail'
import User from '@/components/User'
import VueResource from 'vue-resource'
import VueCookies from 'vue-cookies'

Vue.use(VueCookies)
Vue.use(VueResource)
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: '/',
      component: Main,
      redirect: '/index',
      children: [
        {
          path: 'contest/create',
          name: '/contest/create',
          component: ContestCreate
        },
        {
          path: 'contest/list',
          name: '/contest/list',
          component: ContestList
        },
        {
          path: 'contest/detail/:id',
          name: '/contest/detail/:id',
          component: ContestDetail
        },
        {
          path: 'index',
          name: '/index',
          component: Index
        },
        {
          path: 'login',
          name: '/login',
          component: Login
        },
        {
          path: 'register',
          name: '/register',
          component: Register
        },
        {
          path: 'user',
          name: '/user',
          component: User
        }
      ]
    }
  ]
})
