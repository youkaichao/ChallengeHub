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

Vue.use(ElementUI)
Vue.use(VueCookies)
Vue.use(VueResource)
Vue.use(mavonEditor)

// if (process.env.NODE_ENV !== 'production') {
// Vue.use(VueResourceMock, MockData)
// }

Vue.config.productionTip = false

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
