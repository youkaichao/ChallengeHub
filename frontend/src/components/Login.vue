<template>
  <el-row>
    <el-col :span="8"></el-col>
    <el-col :span="8">
      <el-form ref="form" :model="account" label-width="80px">
        <el-form-item label="用户名">
          <el-input v-model="account.username"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="account.password" type="password"></el-input>
        </el-form-item>
        <el-row>
          <el-col :span="12">
            <el-form-item>
              <el-button type="primary" @click="handleLogin">登录</el-button>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item>
              <el-button type="text" @click="handleRegister">没有账号? 点击注册</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </el-col>
    <el-col :span="8"></el-col>
  </el-row>
</template>
<script>
export default {
  name: 'Login',
  data() {
    return {
      account: {
        username: null,
        password: null
      }
    }
  },
  methods: {
    handleLogin() {
      this.$http.post('/auth/login', this.account).then(function(response) {
        if (response.body.code > 0) {
          this.$message.error('Login failed with error: ' + response.body.error)
          return
        }
        this.$store.commit('login', response.body.data)
        this.$router.push('/user')
      })
    },
    handleRegister() {
      this.$router.push('/register')
    }
  }
}
</script>