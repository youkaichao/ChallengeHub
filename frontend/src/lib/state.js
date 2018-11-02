import Vuex from "vuex";
import Vue from "vue";

// [vuex] must call Vue.use(Vuex) before creating a store instance.
Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    username: null,
    email: null,
    selfDescription: null,
    sourceSchool: null,
    isOrganizer: null,
    login: false
  },
  mutations: {
    login(state, payload) {
      state.username = payload.username;
      state.email = payload.email;
      state.selfDescription = payload.selfDescription;
      state.sourceSchool = payload.sourceSchool;
      state.isOrganizer = payload.isOrganizer;
      state.login = true;
    },
    logout(state, payload) {
      state.username = null;
      state.email = null;
      state.selfDescription = null;
      state.sourceSchool = null;
      state.isOrganizer = null;
      state.login = false;
    }
  }
});
