// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueCookies from 'vue-cookies'
import VueResource from 'vue-resource'
import VueResourceMock from 'vue-resource-mock'
import MockData from '@/lib/api.js'
import store from '@/lib/state.js'
import ElementUI from 'element-ui'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import 'element-ui/lib/theme-chalk/index.css'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faThumbsUp as stu, faThumbsDown as std, faLock, faLockOpen, faUser } from '@fortawesome/free-solid-svg-icons'
import { faThumbsUp as rtu, faThumbsDown as rtd } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import Raven from 'raven-js'
import RavenVue from 'raven-js/plugins/vue'

Vue.use(ElementUI)
Vue.use(VueCookies)
Vue.use(VueResource)
Vue.use(mavonEditor)
Vue.component('font-awesome-icon', FontAwesomeIcon)

library.add(stu, std, rtu, rtd, faLock, faLockOpen, faUser)

if (process.env.NODE_ENV !== 'production') {
  Vue.use(VueResourceMock, MockData)
}

Vue.config.productionTip = false

Raven.config('https://1b42a80d1f924d6bb761d7f878c5157a@sentry.io/1358389')
  .addPlugin(RavenVue, Vue)
  .install()

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
