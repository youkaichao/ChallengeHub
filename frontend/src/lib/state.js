import Vuex from 'vuex'
import Vue from 'vue'

// [vuex] must call Vue.use(Vuex) before creating a store instance.
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: null,
    email: null,
    introduction: null,
    school: null,
    individual: null,
    login: false
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
    logout(state, payload) {
      state.username = null
      state.email = null
      state.introduction = null
      state.school = null
      state.individual = null
      state.login = false
    }
  }
})
