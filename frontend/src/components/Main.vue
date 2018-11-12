<template>
  <el-container class="main-container">
    <el-header height="100">
      <el-row type="flex" :gutter="10">
        <router-link to='/'>
          <span class="logo">
            <span style="font-weight: 800">Challenge</span><span style="font-weight: 100">Hub</span>
          </span>
        </router-link>
        <el-button style="margin-left: auto; margin-top: auto; margin-bottom: auto;" v-if="!login" type="primary" @click="handleRoute('/login')">登录</el-button>
        <el-button style="margin-top: auto; margin-bottom: auto;" v-if="!login" type="primary" @click="handleRoute('/register')">注册</el-button>
        <el-button style="margin-left: auto; margin-top: auto; margin-bottom: auto;" v-if="login" type="primary" @click="handleRoute('/user')">用户中心</el-button>
        <el-button style="margin-top: auto; margin-bottom: auto;" v-if="login" type="primary" @click="handleLogout">登出</el-button>
      </el-row>
    </el-header>
    <router-view></router-view>
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
    }
  },
  created: function() {
    if (!this.$store.state.login && this.$cookies.isKey('username')) {
      let response = this.$http
        .get('/auth/info', {
          params: { username: this.$cookies.get('username') }
        })
        .then(function(response) {
          this.$store.commit('login', response.body.data)
        })
    }
  },
  methods: {
    handleLogout() {
      this.$http.post('/auth/logout', {}).then(function(response) {
        if (response.body.code > 0) {
          alert('Logout faild with error: ' + response.body.error)
          return
        }
        this.$cookies.remove('usename')
        this.$store.commit('logout', response.body.data)
        this.$router.push('/')
      })
    },
    handleRoute(path) {
      this.$router.push({ name: path })
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Titillium+Web:extra-light');
@import url('https://fonts.googleapis.com/css?family=Titillium+Web:semi-bold');

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
</style>