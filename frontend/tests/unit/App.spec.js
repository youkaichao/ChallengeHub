import { shallowMount, createLocalVue } from '@vue/test-utils'
import Vuex from 'vuex'
import ElementUI from 'element-ui'

import App from '@/App.vue'

const localVue = createLocalVue()
localVue.use(Vuex)
localVue.use(ElementUI)

describe('test for App.vue', () => {
  let store
  beforeEach(() => {
    store = new Vuex.Store({
      state: {
        username: null,
        email: null,
        introduction: null,
        school: null,
        individual: null,
        login: false,
        unreadCount: 0
      }
    })
  })

  it('App.vue should has a div with id "app"', () => {
    const wrapper = shallowMount(App, { store, localVue, stubs: ['router-link', 'router-view'] })
    expect(wrapper.contains('div#app')).toBe(true)
  })
})
