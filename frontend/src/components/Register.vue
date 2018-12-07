<template>
  <el-row>
    <el-col :span="5"></el-col>
    <el-col :span="14">
      <el-tabs
        v-model="activeTab"
        @tab-click="handleClick"
      >
        <el-tab-pane
          label="注册学生账号"
          name="student"
        >
          <el-row>
            <el-col :span="14">
              <el-form
                ref="form_individual"
                :rules="rules"
                :model="user"
                label-width="120px"
              >
                <el-form-item
                  label="用户名"
                  prop="username"
                >
                  <el-input v-model="user.username"></el-input>
                </el-form-item>
                <el-form-item
                  label="注册邮箱"
                  prop="email"
                >
                  <el-input v-model="user.email"></el-input>
                </el-form-item>
                <el-form-item
                  label="密码"
                  prop="password"
                >
                  <el-input
                    v-model="user.password"
                    type="password"
                  ></el-input>
                </el-form-item>
                <el-form-item
                  label="确认密码"
                  prop="passwordAgain"
                >
                  <el-input
                    v-model="passwordAgain"
                    type="password"
                  ></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button
                    type="primary"
                    @click="handleCreateAccount('individual')"
                  >创建账号</el-button>
                </el-form-item>
              </el-form>
            </el-col>
            <el-col :span="1"></el-col>
            <el-col :span="9">
              <el-card class="box-card">
                <div
                  slot="header"
                  class="clearfix"
                >
                  <span><i class="el-icon-info"></i> 通过注册你可以</span>
                </div>
                <div class="card-item">报名竞赛</div>
                <div class="card-item">讨论区留言</div>
              </el-card>
            </el-col>
          </el-row>
        </el-tab-pane>
        <el-tab-pane
          label="注册组织者账号"
          name="organization"
        >
          <el-row>
            <el-col :span="14">
              <el-form
                ref="form_organization"
                :rules="rules"
                :model="user"
                label-width="120px"
              >
                <el-form-item
                  label="用户名"
                  prop="username"
                >
                  <el-input v-model="user.username"></el-input>
                </el-form-item>
                <el-form-item
                  label="机构邮箱"
                  prop="email"
                >
                  <el-input v-model="user.email"></el-input>
                </el-form-item>
                <el-form-item
                  label="密码"
                  prop="password"
                >
                  <el-input
                    v-model="user.password"
                    type="password"
                  ></el-input>
                </el-form-item>
                <el-form-item
                  label="重新输入密码"
                  prop="passwordAgain"
                >
                  <el-input
                    v-model="passwordAgain"
                    type="password"
                  ></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button
                    type="primary"
                    @click="handleCreateAccount('organization')"
                  >创建账号</el-button>
                </el-form-item>
              </el-form>
            </el-col>
            <el-col :span="1"></el-col>
            <el-col :span="9">
              <el-card class="box-card">
                <div
                  slot="header"
                  class="clearfix"
                >
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
    let validatePass = (rule, value, callback) => {
      if (this.user.password !== this.passwordAgain) {
        callback(new Error('两次输入的密码不一致'))
      } else {
        callback()
      }
    }
    return {
      user: {
        username: null,
        email: null,
        password: null,
        individual: null
      },
      passwordAgain: null,
      activeTab: 'student',
      rules: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          {
            validator: (rule, value, callback) => {
              if (value.includes('&')) {
                callback(new Error('用户名不能包含&字符'))
              } else {
                callback()
              }
            },
            trigger: 'change'
          }
        ],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
        passwordAgain: [{ required: true, validator: validatePass, trigger: 'blur' }],
        email: [{ required: true, message: '请输入邮箱', trigger: 'blur' }, { type: 'email', message: '邮箱必须合法', trigger: 'change' }]
      }
    }
  },
  methods: {
    handleCreateAccount(type) {
      this.user.individual = type
      let formName = type === 'individual' ? 'form_individual' : 'form_organization'
      this.$refs[formName].validate(valid => {
        if (valid) {
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
        } else {
          this.$message.error('表单有误，请修改后提交')
          return false
        }
      })
    },
    handleClick(tab) {
      this.activeTab = tab.name
    }
  }
}
</script>

