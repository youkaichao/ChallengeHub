<template>
  <div style="width: 600px; margin: auto;">
    <div>
      <h2>基本比赛信息</h2>
      <el-form>
        <el-form-item v-for="(formItem, idx) in enrollFormItems" :key="idx" :label="formItem.label">
          <el-input :placeholder="formItem.description" v-model="formAnswers[idx]"></el-input>
        </el-form-item>
      </el-form>
    </div>
    <div style="margin-top: 150px;">
      <h2>队伍组成信息</h2>
      <el-form>
        <el-form-item label="队伍名称">
          <el-input placeholder="输入队伍名称" v-model="groupName"></el-input>
        </el-form-item>
      </el-form>

      <el-alert title="请勿在下面的队伍成员中添加自己" type="warning" class="warning-box"></el-alert>
      <el-alert title="作为填写者，你将自动成为该队伍的队长" type="warning" class="warning-box"></el-alert>
      <el-form>

        <el-card class="box-card">
          <div slot="header" style="text-align: left;">
            <b>队伍成员</b>
          </div>
          <div v-for="(userId, idx) in groupMembersExcludeLeader" :key="idx" class="text item" style="text-align: left;">
            {{ userId }}
          </div>
        </el-card>

        <el-row>
          <el-col :span="20">
            <el-input placeholder="希望添加的队员名称" v-model="newMemberId"></el-input>
          </el-col>
          <el-col :span="4">
            <el-button type="primary" @click="addNewMember">添加</el-button>
          </el-col>
        </el-row>
      </el-form>
    </div>

    <div style="margin-top: 150px; margin-bottom: 50px;">
      <h2>完成报名</h2>
      <el-button type="primary" @click="enrollSubmit">确认报名</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContestEnroll',
  created() {
    // TODO created function here
  },
  data() {
    return {
      enrollForm: '{}',
      formAnswers: [],
      newMemberId: null,
      groupName: null,
      groupMembersExcludeLeader: []
    }
  },
  created: async function() {
    let contestId = this.$route.params.id
    let response = await this.$http.get(`/api/contests/${contestId}/enroll`)
    this.enrollForm = response.body.data.enrollForm
  },
  methods: {
    addNewMember: function() {
      let userId = this.newMemberId
      this.newMemberId = null
      this.groupMembersExcludeLeader.push(userId)
    },
    enrollSubmit: async function() {
      let contestId = this.$route.params.id
      let form = {}
      for (let i = 0; i < this.enrollFormItems.length; i++) {
        form[this.enrollFormItems[i]['label']] = this.formAnswers[i]
      }
      var realMembers = this.groupMembersExcludeLeader.slice()
      realMembers.push(this.$store.state.username)
      let postData = {
        name: this.groupName,
        leaderName: this.$store.state.username,
        members: realMembers,
        form: JSON.stringify(form)
      }
      let response = await this.$http.post(`/api/contests/${contestId}/enroll`, postData)
      if (response.body.code !== 0) {
        alert(response.body.error)
      } else {
        this.$router.push('/index')
      }
    }
  },
  computed: {
    enrollFormItems: function() {
      let enrollForm = JSON.parse(this.enrollForm)
      let ret = []
      for (let key in enrollForm) {
        ret.push({ label: key, description: enrollForm[key] })
      }
      return ret
    }
  },
  watch: {
    enrollFormItems: function(val) {
      this.formAnswers = [...Array(val.length)].map((_, __) => '')
    }
  }
}
</script>

<style scope>
.warning-box {
  margin-top: 20px !important;
  margin-bottom: 20px !important;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}
</style>
