import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Index from '@/components/Index'
import Login from '@/components/Login'
import Register from '@/components/Register'
import ContestView from '@/components/contest/ContestView'
import ContestCreate from '@/components/contest/ContestCreate'
import ContestDetail from '@/components/contest/ContestDetail'
import ContestEnroll from '@/components/contest/ContestEnroll'
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
          component: ContestView
        },
        {
          path: 'contest/detail/:id',
          name: '/contest/detail/:id',
          component: ContestDetail
        },
        {
          path: 'contest/enroll/:id',
          name: '/contest/enroll/:id',
          component: ContestEnroll
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
