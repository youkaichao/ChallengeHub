<template>
  <div style="width: 600px; margin: auto;">
    <div>
      <h2>基本比赛信息</h2>
      <el-form>
        <el-form-item
          v-for="(formItem, idx) in enrollFormItems"
          :key="idx"
          :label="formItem.label"
        >
          <el-input
            v-if="formItem.type==='文字题'"
            :placeholder="formItem.description"
            v-model="formAnswers[idx]"
          ></el-input>
          <el-select
            v-if="formItem.type==='选择题'"
            placeholder="请选择"
            v-model="formAnswers[idx]"
          >
            <el-option
              v-for="item of formItem.options"
              :key="item"
              :label="item"
              :value="item"
            >
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
    </div>
    <div style="margin-top: 150px;">
      <h2>队伍组成信息</h2>
      <el-form>
        <el-form-item label="队伍名称">
          <el-input
            placeholder="输入队伍名称"
            v-model="groupName"
          ></el-input>
        </el-form-item>
      </el-form>
    </div>

    <div style="margin-top: 150px; margin-bottom: 50px;">
      <h2>完成报名</h2>
      <el-button
        type="primary"
        @click="enrollSubmit"
      >确认报名</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ContestEnroll',
  data() {
    return {
      enrollForm: '[]',
      formAnswers: [],
      newMemberId: null,
      groupName: null,
      groupMembersExcludeLeader: []
    }
  },
  created: async function() {
    let contestId = this.$route.params.id
    let response = await this.$http.get(`/api/contests/${contestId}/enroll`)
    if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
    }
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
        if (!this.formAnswers[i]) {
          this.$message({ type: 'error', message: `请填写${this.enrollFormItems[i]['label']}` })
          return
        }
        form[this.enrollFormItems[i]['label']] = this.formAnswers[i]
      }
      if (!this.groupName) {
        this.$message({ type: 'error', message: '请填写队名' })
        return
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
        this.$alert(response.body.error)
      } else {
        this.$router.push('/index')
      }
    }
  },
  computed: {
    enrollFormItems: function() {
      let enrollForm = JSON.parse(this.enrollForm)
      let ret = []
      for (let item of enrollForm) {
        ret.push({ label: item.label, description: item.description, type: item.formType, options: item.options })
      }
      return ret
    }
  },
  watch: {
    enrollFormItems: function(val) {
      this.formAnswers = [...Array(val.length)].map(() => '')
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
