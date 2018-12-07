import Vue from 'vue'
import Router from 'vue-router'
const Main = () => import('@/components/Main')
const Index = () => import('@/components/Index')
const Login = () => import('@/components/Login')
const Register = () => import('@/components/Register')
const ContestView = () => import('@/components/contest/ContestView')
const ContestCreate = () => import('@/components/contest/ContestCreate')
const ContestDetail = () => import('@/components/contest/ContestDetail')
const ContestEnroll = () => import('@/components/contest/ContestEnroll')
const ContestNoticeList = () => import('@/components/contest/ContestNoticeList')
const JudgeWorkspace = () => import('@/components/workspace/JudgeWorkspace')
const User = () => import('@/components/User')
const ControlPanel = () => import('@/components/organizer/ControlPanel')
const VueResource = () => import('vue-resource')
const VueCookies = () => import('vue-cookies')
const ManageGroup = () => import('@/components/organizer/ManageGroup')
const ManageJudge = () => import('@/components/organizer/ManageJudge')
const Overview = () => import('@/components/organizer/Overview')
const ManageSubmission = () => import('@/components/organizer/ManageSubmission')
const NoticeList = () => import('@/components/organizer/NoticeList')
const GroupInfo = () => import('@/components/organizer/GroupInfo')
const ManageReview = () => import('@/components/organizer/ManageReview')
const NoticeDetail = () => import('@/components/organizer/NoticeDetail')
const NewNotice = () => import('@/components/organizer/NewNotice')
const UserValidation = () => import('@/components/UserValidation')
const MessageCenter = () => import('@/components/messaging/MessageCenter')
const NewMessage = () => import('@/components/messaging/NewMessage')
const GroupDashboard = () => import('@/components/dashboard/GroupDashboard')
const GroupList = () => import('@/components/dashboard/GroupList')
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
          path: 'validate/:token',
          name: '/validate/:token',
          component: UserValidation
        },
        {
          path: 'message',
          name: '/message',
          component: MessageCenter
        },
        {
          path: 'message/new',
          name: '/message/new',
          component: NewMessage
        },
        {
          path: 'message/new/:peer',
          name: '/message/new/:peer',
          component: NewMessage
        },
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
          path: 'contest/notice/:id',
          name: '/contest/notice/:id',
          component: ContestNoticeList
        },
        {
          path: 'contest/enroll/:id',
          name: '/contest/enroll/:id',
          component: ContestEnroll
        },
        {
          path: 'contest/:id/mygroup',
          name: 'mygroup',
          component: GroupDashboard
        },
        {
          path: 'contest/:id/grouplist',
          name: 'grouplist',
          component: GroupList
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
          path: 'organizer/:id',
          component: ControlPanel,
          children: [
            {
              path: 'managegroup',
              name: 'managegroup',
              component: ManageGroup
            },
            {
              path: 'managejudge',
              name: 'managejudge',
              component: ManageJudge
            },
            {
              path: '',
              name: 'overview',
              component: Overview
            },
            {
              path: 'managereview',
              name: 'managereview',
              component: ManageReview
            },
            {
              path: 'managesubmission',
              name: 'managesubmission',
              component: ManageSubmission
            },
            {
              path: 'notices',
              name: 'notices',
              component: NoticeList
            },
            {
              path: 'notices/:noticeId',
              name: 'noticedetail',
              component: NoticeDetail
            },
            {
              path: 'notices/newnotice',
              name: 'newnotice',
              component: NewNotice
            },
            {
              path: 'groupinfo',
              name: 'groupinfo',
              component: GroupInfo
            }
          ]
        },
        {
          path: 'judge/workspace/:id',
          name: '/judge/workspace/:id',
          component: JudgeWorkspace
        }
      ]
    }
  ]
})
