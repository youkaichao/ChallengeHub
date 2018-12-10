<template>
  <el-container class="main-container">
    <el-header height="100">
      <el-row type="flex" :gutter="10">
        <router-link to="/">
          <span class="logo">
            <span style="font-weight: 800">Challenge</span>
            <span style="font-weight: 100">Hub</span>
          </span>
        </router-link>
        <el-button
          style="margin-left: auto; margin-top: auto; margin-bottom: auto;"
          v-if="!login"
          type="primary"
          @click="handleRoute('/login')"
        >登录</el-button>
        <el-button
          style="margin-top: auto; margin-bottom: auto;"
          v-if="!login"
          type="primary"
          @click="handleRoute('/register')"
        >注册</el-button>
        <el-badge
          :value="unreadCount"
          style="margin-left: auto; margin-top: auto; margin-bottom: auto;"
          v-if="login && unreadCount !== 0"
        >
          <el-button type="primary" @click="handleRoute('/message')">消息中心</el-button>
        </el-badge>
        <el-button
          type="primary"
          v-if="login && unreadCount === 0"
          style="margin-left: auto; margin-top: auto; margin-bottom: auto;"
          @click="handleRoute('/message')"
        >消息中心</el-button>
        <el-button
          style="margin-top: auto; margin-bottom: auto; margin-left: 10px;"
          v-if="login"
          type="primary"
          @click="handleRoute('/user')"
        >用户中心</el-button>
        <el-button
          style="margin-top: auto; margin-bottom: auto; margin-left: 10px;"
          v-if="login"
          type="primary"
          @click="handleLogout"
        >登出</el-button>
      </el-row>
    </el-header>
    <transition name="component-fade" mode="out-in">
      <router-view></router-view>
    </transition>
    <el-row align="middle">
      <el-button type="text" @click="handleRoute('/about')">关于我们</el-button>
      <el-button type="text" @click="handleRoute('/help')">帮助中心</el-button>
    </el-row>
  </el-container>
</template>
<script>
export default {
  name: 'Main',
  computed: {
    login: function() {
      return this.$store.state.login
    },
    unreadCount() {
      return this.$store.state.unreadCount
    }
  },
  created: async function() {
    if (!this.$store.state.login) return
    let response = await this.$http.get('/apiv2/messages/unread_count')
    if (response.body.code !== 0) {
      this.$message({ type: 'error', message: response.body.error })
      return
    }
    this.$store.commit('setUnreadCount', response.body.data)
  },
  methods: {
    handleLogout() {
      this.$http.post('/auth/logout', {}).then(function(response) {
        this.$store.commit('logout', response.body.data)
        this.$router.push('/')
        if (response.body.code > 0) {
          this.$alert('Logout faild with error: ' + response.body.error)
          return
        }
      })
    },
    handleRoute(path) {
      this.$router.push({ name: path })
    }
  }
}
</script>

<style>
@font-face {
  font-family: 'Titillium Web';
  src: url('../../fonts/TitilliumWeb-ExtraLight.ttf') format('truetype');
  font-weight: 100;
}

@font-face {
  font-family: 'Titillium Web';
  src: url('../../fonts/TitilliumWeb-SemiBold.ttf') format('truetype');
  font-weight: 800;
}

.logo {
  font-family: 'Titillium Web';
  font-size: 300%;
  text-align: left;
  padding-left: 0px;
  margin: 0px;
}

.main-container {
  width: 1200px;
  margin: 0 auto;
  padding: 0;
}

.component-fade-enter-active, .component-fade-leave-active {
  transition: opacity .3s ease;
}
.component-fade-enter, .component-fade-leave-to
/* .component-fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>