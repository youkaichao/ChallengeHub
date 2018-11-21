<template>
  <el-row>
    <el-col :span="5"></el-col>
    <el-col :span="14">
      <el-tabs v-model="activeTab" @tab-click="handleClick">
        <el-tab-pane label="注册学生账号" name="student">
          <el-row>
            <el-col :span="14">
              <el-form ref="form" :model="user" label-width="80px">
                <el-form-item label="用户名">
                  <el-input v-model="user.username"></el-input>
                </el-form-item>
                <el-form-item label="注册邮箱">
                  <el-input v-model="user.email"></el-input>
                </el-form-item>
                <el-form-item label="密码">
                  <el-input v-model="user.password" type="password"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="handleCreateAccount('individual')">创建账号</el-button>
                </el-form-item>
              </el-form>
            </el-col>
            <el-col :span="1"></el-col>
            <el-col :span="9">
              <el-card class="box-card">
                <div slot="header" class="clearfix">
                  <span><i class="el-icon-info"></i> 通过注册你可以</span>
                </div>
                <div class="card-item">报名竞赛</div>
                <div class="card-item">讨论区留言</div>
              </el-card>
            </el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane label="注册组织者账号" name="organization">
          <el-row>
            <el-col :span="14">
              <el-form ref="form" :model="user" label-width="80px">
                <el-form-item label="用户名">
                  <el-input v-model="user.username"></el-input>
                </el-form-item>
                <el-form-item label="机构邮箱">
                  <el-input v-model="user.email"></el-input>
                </el-form-item>
                <el-form-item label="密码">
                  <el-input v-model="user.password" type="password"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="handleCreateAccount('organization')">创建账号</el-button>
                </el-form-item>
              </el-form>
            </el-col>
            <el-col :span="1"></el-col>
            <el-col :span="9">
              <el-card class="box-card">
                <div slot="header" class="clearfix">
                  <span><i class="el-icon-info"></i> 通过注册你可以</span>
                </div>
                <div class="card-item">发布竞赛/活动</div>
                <div class="card-item">自定义报名系统</div>
                <div class="card-item">竞赛/活动报名管理</div>
              </el-card>
            </el-col>
          </el-row>
        </el-tab-pane>
      </el-tabs>
    </el-col>
    <el-col :span="5">
    </el-col>
  </el-row>
</template>
<script>
export default {
  name: 'Register',
  data() {
    return {
      user: {
        username: null,
        email: null,
        password: null,
        individual: null
      },
      activeTab: 'student'
    }
  },
  methods: {
    handleCreateAccount(type) {
      this.user.individual = type
      this.$http.post('/auth/register', this.user).then(function(response) {
        if (response.data.code > 0) {
          this.$alert('Register failed with error: ' + response.data.error)
          return
        }
        this.$message({
          message: '我们已经向您的注册邮箱中发送了一封验证邮件，请尽快点击邮件中验证链接以激活您的账号',
          type: 'warning'
        })
        this.$router.push('/')
      })
    },
    handleClick(tab) {
      this.activeTab = tab.name
    }
  }
}
</script>

