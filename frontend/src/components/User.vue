<template>
  <el-tabs v-model="activeName" tab-position="left">
    <el-tab-pane :label="user.individual ? '个人基本信息':'机构基本信息'" name="userInfo">
      <el-row v-if="user.individual">
        <el-col :span="6"></el-col>
        <el-col :span="12">
          <el-row type="flex" align="middle">
            <el-col :span="4"><label> 邮箱 </label></el-col>
            <el-col :span="20">
              <el-input :value="user.email"> </el-input>
            </el-col>
          </el-row>
          <el-row type="flex" align="middle">
            <el-col :span="4"><label> 简介 </label></el-col>
            <el-col :span="20">
              <el-input :value="user.introduction"> </el-input>
            </el-col>
          </el-row>
          <el-row type="flex" align="middle">
            <el-col :span="4"><label> 学校 </label></el-col>
            <el-col :span="20">
              <el-input :value="user.school"> </el-input>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="8"></el-col>
            <el-col :span="8">
              <el-button type="primary" @click="handleChange">修改</el-button>
            </el-col>
            <el-col :span="8"></el-col>
          </el-row>
        </el-col>
        <el-col :span="6"></el-col>
      </el-row>
      <el-row v-if="!user.individual">
        <el-col :span="6"></el-col>
        <el-col :span="12">
          <el-row type="flex" align="middle">
            <el-col :span="4"><label> 邮箱 </label></el-col>
            <el-col :span="20">
              <el-input :value="user.email"> </el-input>
            </el-col>
          </el-row>
          <el-row type="flex" align="middle">
            <el-col :span="4"><label> 简介 </label></el-col>
            <el-col :span="20">
              <el-input :value="user.introduction"> </el-input>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="8"></el-col>
            <el-col :span="8">
              <el-button type="primary" @click="handleChange">修改</el-button>
            </el-col>
            <el-col :span="8"></el-col>
          </el-row>
        </el-col>
        <el-col :span="6"></el-col>
      </el-row>
    </el-tab-pane>
    <el-tab-pane v-if="user.individual" label="我参与的比赛" name="myContest">
      <ContestView :data-list="user.myContestView" />
    </el-tab-pane>
    <el-tab-pane v-if="user.individual" label="我评审的比赛" name="contestIReview">
      <ContestView :data-list="user.contestIReviewList" />
    </el-tab-pane>
    <el-tab-pane v-if="!user.individual" label="我发起的比赛" name="contestILaunch">
      <ContestView :data-list="user.contestIReviewList" />
    </el-tab-pane>
    <el-tab-pane label="修改密码" name="resetPassword">
      <el-row>
        <el-col :span="6"></el-col>
        <el-col :span="12">
          <el-row type="flex" align="middle">
            <el-col :span="4"><label> 原密码 </label></el-col>
            <el-col :span="20">
              <el-input type="password" id="oldPassword"> </el-input>
            </el-col>
          </el-row>
          <el-row type="flex" align="middle">
            <el-col :span="4"><label> 新密码 </label></el-col>
            <el-col :span="20">
              <el-input type="password" id="newPassword"> </el-input>
            </el-col>
          </el-row>
          <el-row type="flex" align="middle">
            <el-col :span="4"><label> 确认新密码 </label></el-col>
            <el-col :span="20">
              <el-input type="password" id="confirmPassword"> </el-input>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="8"></el-col>
            <el-col :span="8">
              <el-button type="primary" @click="handleResetPassword">修改</el-button>
            </el-col>
            <el-col :span="8"></el-col>
          </el-row>
        </el-col>
        <el-col :span="6"></el-col>
      </el-row>
    </el-tab-pane>
  </el-tabs>
</template>
<script>
import ContestView from '@/components/contest/ContestView'
export default {
  name: 'User',
  data() {
    return {
      activeName: 'userInfo',
      user: {
        username: this.$store.state.username,
        email: this.$store.state.email,
        introduction: this.$store.state.introduction,
        school: this.$store.state.school,
        individual: this.$store.state.individual,
        oldPassword: '',
        newPassword: '',
        myContestView: [
          {
            name: '',
            subject: '',
            contestID: ''
          }
        ],
        contestIReviewList: [],
        contestILaunch: []
      }
    }
  },
  methods: {
    handleChange() {},
    handleResetPassword() {}
  },
  components: {
    ContestView
  }
}
</script>
<style>
.el-row {
  margin-bottom: 20px;
}
</style>