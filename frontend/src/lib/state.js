import Vuex from 'vuex'
import Vue from 'vue'
import VuexPersistence from 'vuex-persist'

// [vuex] must call Vue.use(Vuex) before creating a store instance.
Vue.use(Vuex)

const vuexLocal = new VuexPersistence({
  storage: window.localStorage
})

export default new Vuex.Store({
  state: {
    username: null,
    email: null,
    introduction: null,
    school: null,
    individual: null,
    login: false,
    unreadCount: 0
  },
  mutations: {
    login(state, payload) {
      state.username = payload.username
      state.email = payload.email
      state.introduction = payload.introduction
      state.school = payload.school
      state.individual = payload.individual
      state.login = true
    },
    logout(state) {
      state.username = null
      state.email = null
      state.introduction = null
      state.school = null
      state.individual = null
      state.login = false
    },
    setUnreadCount(state, payload) {
      state.unreadCount = payload.count
    },
    decreaseUnreadCount(state) {
      state.unreadCount = state.unreadCount - 1
    }
  },
  plugins: [vuexLocal.plugin]
})
