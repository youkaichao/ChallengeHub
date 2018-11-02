<template>
  <el-container>
    <el-header height="100">
      <el-row type="flex" align="middle" :gutter="10">
        <el-col :span="4">
          <router-link to='/'>
            <h1>
              <b>Challenge</b> Hub
            </h1>
          </router-link>
        </el-col>
        <div>
          <el-menu :default-active="$route.path" mode="horizontal" :router="true">
            <el-menu-item index="/index">首页</el-menu-item>
            <el-menu-item index="/contest/list">查看比赛</el-menu-item>
            <el-menu-item index="/contest/create">创建比赛</el-menu-item>
          </el-menu>
        </div>
        <el-col :span="11">
          <el-input v-model="input" placeholder="搜索比赛"></el-input>
        </el-col>
        <el-col :span="1">
          <el-button icon="el-icon-search" circle></el-button>
        </el-col>
        <el-col :span="1.5" v-if="!login">
          <el-button type="primary" @click="handleRoute('/login')">登录</el-button>
        </el-col>
        <el-col :span="1.5" v-if="!login">
          <el-button type="primary" @click="handleRoute('/register')">注册</el-button>
        </el-col>
        <el-col :span="1.5" v-if="login">
          <el-button type="primary" @click="handleRoute('/user')">用户中心</el-button>
        </el-col>
        <el-col :span="1.5" v-if="login">
          <el-button type="primary" @click="handleLogout">登出</el-button>
        </el-col>
      </el-row>
    </el-header>
    <el-main>
      <router-view :data-list="contestList" v-on:onUpdateList="updateList"></router-view>
    </el-main>
    <el-footer>
      <el-row type="flex" align="middle">
        <el-col :span="12">
          <el-button type="text" @click="handleRoute('/about')">关于我们</el-button>
        </el-col>
        <el-col :span="12">
          <el-button type="text" @click="handleRoute('/help')">帮助中心</el-button>
        </el-col>
      </el-row>
    </el-footer>
  </el-container>
</template>
<script>
export default {
  name: 'Main',
  data() {
    return {
      input: '',
      contestList: [
        {
          id: null,
          name: null,
          subject: null
        }
      ]
    }
  },
  computed: {
    login: function() {
      return this.$store.state.login
    }
  },
  methods: {
    handleLogout() {
      this.$http.post('/auth/logout').then(function(response) {
        if (response.body.code > 0) {
          alert('Logout faild with error: ' + response.body.error)
          return
        }
        this.$store.commit('logout', response.body.data)
        this.$router.push('/')
      })
    },
    updateList() {
      this.$http.get('/api/contest').then(function(response) {
        this.contestList = JSON.parse(response.body.data)
      })
    },
    handleRoute(path) {
      this.$router.push({ name: path })
    }
  }
}
</script>
