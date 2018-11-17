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
import CompetitorDashboard from '@/components/dashboard/CompetitorDashboard'
import JudgeDashboard from '@/components/dashboard/JudgeDashboard'
import JudgeWorkspace from '@/components/workspace/JudgeWorkspace'
import User from '@/components/User'
import ControlPanel from '@/components/organizer/ControlPanel'
import VueResource from 'vue-resource'
import VueCookies from 'vue-cookies'
import ManageGroup from '@/components/organizer/ManageGroup'
import Overview from '@/components/organizer/Overview'
import MyOrganizeContests from '@/components/organizer/MyOrganizeContests'

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
        },
        {
          path: 'organizer',
          name: '/organizer',
          component: MyOrganizeContests
        },
        {
          path: 'organizer/controlpanel/:id',
          name: '/organizer/controlpanel',
          component: ControlPanel,
          children: [
            {
              path: 'managegroup',
              name: '/organizer/controlpanel/:id/managegroup',
              component: ManageGroup
            },
            {
              path: '',
              name: '/organizer/controlpanel/:id',
              component: Overview
            }
          ]
        },
        {
          path: 'competitor_dashboard',
          name: '/competitor_dashboard',
          component: CompetitorDashboard
        },
        {
          path: 'judge_dashboard',
          name: '/judge_dashboard',
          component: JudgeDashboard
        },
        {
          path: 'judge/workspace/:id/',
          component: JudgeWorkspace
        }
      ]
    }
  ]
})
