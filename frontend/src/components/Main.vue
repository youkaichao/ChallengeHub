<template>
  <el-container>
    <el-header height="100">
      <el-row type="flex" align="middle" :gutter="1">
        <el-col :span="4">
          <router-link to='/'>
            <h1>
              <b>Challenge</b> Hub
            </h1>
          </router-link>
        </el-col>
        <el-col :span="5">
          <el-menu :default-active="$route.path" mode="horizontal" @select="handleSelect" :router="true">
            <el-menu-item index="/index">首页</el-menu-item>
            <el-menu-item index="/contest/list">查看比赛</el-menu-item>
            <el-menu-item index="/contest/create">创建比赛</el-menu-item>
          </el-menu>
        </el-col>
        <el-col :span="11">
          <el-input v-model="input" placeholder="搜索比赛"></el-input>
        </el-col>
        <el-col :span="1">
          <el-button icon="el-icon-search" circle></el-button>
        </el-col>
        <el-col :span="1.5">
          <el-button type="primary" @click="handleRoute('/login')">登录</el-button>
        </el-col>
        <el-col :span="1.5">
          <el-button type="primary" @click="handleRoute('/register')">注册</el-button>
        </el-col>
      </el-row>
    </el-header>
    <el-main>
      <router-view :data-list="contestList"></router-view>
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
      contestList: []
    }
  },
  methods: {
    handleSelect(key, keyPath) {},
    handleRoute(path) {
      this.$router.push({ name: path })
    }
  }
}
</script>
