<template>
  <el-row>
    <el-alert v-if="status==0" title="正在认证您的邮箱" type="info" description="请稍候......" show-icon></el-alert>
    <el-alert v-if="status==1" title="邮箱认证成功" type="success" description="您的邮箱验证完毕, 5秒后将前往登陆界面" show-icon>
    </el-alert>
    <el-alert v-if="status==-1" title="邮箱认证失败" type="error" description="邮箱验证失败, 请联系管理员寻求帮助, 5秒后将返回主页" show-icon>
    </el-alert>
  </el-row>
</template>

<script>
export default {
  data() {
    return {
      status: 0
    }
  },
  async created() {
    let token = this.$route.params.token
    let response = await this.$http.post(`/auth/validate`, { token: token })
    if (response.body.code !== 0) {
      let self = this
      this.status = -1
      setTimeout(function() {
        self.$router.push('/')
      }, 5000)
      return
    }
    this.status = 1
    setTimeout(() => {
      this.$router.push('/login')
    }, 5000)
  }
}
</script>

<style scoped>
</style>
