<template>
  <div style="width: 600px; margin: auto;">
    <h2>修改密码</h2>
    <el-form ref="form" :rules="rules" label-width="120px">
      <el-form-item label="原密码" prop="oldPassword">
        <el-input type="password" v-model="oldPassword"></el-input>
      </el-form-item>
      <el-form-item label="新密码" prop="newPassword">
        <el-input type="password" v-model="newPassword"></el-input>
      </el-form-item>
      <el-form-item label="重新输入新密码" prop="repeatNewPassword">
        <el-input type="password" v-model="newPasswordRetyped"></el-input>
      </el-form-item>
    </el-form>
    <el-button type="primary" @click="repasswordConfirm()" style="margin-bottom: 60px;">确认修改密码</el-button>

    <h2>修改学校信息</h2>
    <el-input v-model="profile.school"/>
    <el-button
      style="margin-top: 20px; margin-bottom: 60px;"
      type="primary"
      @click="modSchoolConfim()"
    >确认修改学校</el-button>

    <h2>修改自我简介</h2>
    <el-input type="textarea" v-model="profile.introduction"/>
    <el-button style="margin-top: 20px;" type="primary" @click="modIntroductionConfim()">确认修改简介</el-button>
  </div>
</template>

<script>
export default {
  name: 'ProfileManagement',
  async created() {
    let response = await this.$http.get(`/auth/info`)
    if (response.body.code !== 0) {
      this.$message({ type: 'error', message: response.body.error })
      return
    }
    this.profile = response.body.data
  },
  data() {
    let validatePass = (rule, value, callback) => {
      value = this.newPassword
      if (!value) {
        callback(new Error('请输入新密码'))
      } else {
        callback()
      }
    }
    let validatePass2 = (rule, value, callback) => {
      value = this.newPasswordRetyped
      if (!value) {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.newPassword) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    let validateRequired = (rule, value, callback) => {
      value = this.oldPassword
      if (!value) {
        callback(new Error('请输入密码'))
      } else {
        callback()
      }
    }
    return {
      oldPassword: '',
      newPassword: '',
      newPasswordRetyped: '',
      profile: {},
      rules: {
        oldPassword: [{ validator: validateRequired, trigger: 'blur' }],
        newPassword: [{ validator: validatePass, trigger: 'blur' }],
        repeatNewPassword: [{ validator: validatePass2, trigger: 'blur' }]
      }
    }
  },
  methods: {
    async repasswordConfirm() {
      if (this.newPassword !== this.newPasswordRetyped) {
        this.$message({ type: 'error', message: '两次输入的密码不一致' })
        return
      }
      let response = await this.$http.post(`/auth/reset_password`, {
        old: this.oldPassword,
        new: this.newPassword
      })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      } else {
        this.$message({ type: 'success', message: '修改密码成功' })
        this.oldPassword = ''
        this.newPassword = ''
        this.newPasswordRetyped = ''
        await this.refreshInfo()
      }
    },
    async modSchoolConfim() {
      let response = await this.$http.post(`/auth/info`, {
        school: this.profile.school
      })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
      } else {
        this.$message({ type: 'success', message: '修改学校成功' })
        await this.refreshInfo()
      }
    },
    async modIntroductionConfim() {
      let response = await this.$http.post(`/auth/info`, {
        introduction: this.profile.introduction
      })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
      } else {
        this.$message({ type: 'success', message: '修改个人信息成功' })
        await this.refreshInfo()
      }
    },
    async refreshInfo() {
      let response = await this.$http.get(`/auth/info`)
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      } else {
        this.$store.commit('login', response.body.data)
      }
    }
  }
}
</script>

<style>
</style>
