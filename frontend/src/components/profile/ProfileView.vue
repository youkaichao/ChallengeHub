<template>
  <div style="width: 500px; margin: auto;">
    <h2>用户基本信息</h2>
    <el-row>
      <el-col :span="12" class="theme">用户名</el-col>
      <el-col :span="12">{{ userData.username }}</el-col>
    </el-row>
    <el-row>
      <el-col :span="12" class="theme">邮箱地址</el-col>
      <el-col :span="12">{{ userData.email }}</el-col>
    </el-row>
    <el-row>
      <el-col :span="12" class="theme">学校</el-col>
      <el-col :span="12">{{ userData.school || '（未填写）' }}</el-col>
    </el-row>
    <el-row>
      <el-col :span="12" class="theme">用户类型</el-col>
      <el-col :span="12">{{ userData.individual === 1 ? '个人用户' : '机构用户' }}</el-col>
    </el-row>
    <h2>用户自我简介</h2>
    <el-card>{{ userData.introduction || '（用户未填写简介）' }}</el-card>
    <el-button
      style="margin-top: 40px;"
      type="primary"
      @click="$router.push(`/message/new/${username}`)"
    >向用户发私信</el-button>
  </div>
</template>

<script>
export default {
  name: 'ProfileView',
  data() {
    return {
      userData: {},
      username: ''
    }
  },
  async created() {
    this.username = this.$route.params.username
    let response = await this.$http.get(`/api/users/profile/${this.username}`)
    if (response.body.code !== 0) {
      this.$message({ type: 'error', message: response.body.error })
      return
    }
    this.userData = response.body.data
  }
}
</script>

<style>
.theme {
  color: #409eff;
}
</style>
