<template>
  <div>
    <div style="text-align: left;">
      <el-row type='flex' align-items="center">
        <el-col :span="6" style="text-align: left; margin: auto;"> <span class="info-tag">姓名</span> {{ this.$store.state.username }} </el-col>
        <el-col :span="6" style="text-align: left; margin: auto;"> <span class="info-tag">学校</span> {{ this.$store.state.school }} </el-col>
        <el-col :span="6" style="text-align: left; margin: auto;"> <span class="info-tag">邮箱</span> {{ this.$store.state.email }} </el-col>
        <el-col :span="6" style="text-align: right;">
          <el-button type="text" @click="$router.push('/user')">修改个人信息</el-button>
        </el-col>
      </el-row>
      <el-row type="flex" align-items="center">
        <el-col :span="18" style="text-align: left; margin: auto;">
          <h1 style="font-size: 48px; margin: 0">我参加的比赛</h1>
        </el-col>
        <el-col :span="6" style="text-align: right; margin: auto;">
          <el-button type="primary" plain @click="$router.push('/judge_dashboard')">切换到评委视图</el-button>
        </el-col>
      </el-row>
    </div>
    <el-tabs>
      <el-tab-pane label="未结束的比赛">
        <enrolled-contest-unfinished style="margin-top: 10px;" v-for="info of enrolledUnfinished" :contest="info.contest" :group="info.group" :key="info.contest.id" />
      </el-tab-pane>
      <el-tab-pane label="已结束的比赛">
        <enrolled-contest-finished style="margin-top: 10px;" v-for="info of enrolledFinished" :contest="info.contest" :group="info.group" :key="info.contest.id" />
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import EnrolledContestUnfinished from './EnrolledContestUnfinished.vue'
import EnrolledContestFinished from './EnrolledContestFinished.vue'

export default {
  name: 'CompetitorDashboard',
  data() {
    return {
      enrolledContestsAndGroups: []
    }
  },
  async created() {
    let response = await this.$http.get('/api/users/enrolled')
    if (response.body.code !== 0) {
      this.$message.error({ type: 'error', message: response.body.error })
      return
    }
    this.enrolledContestsAndGroups = response.body.data

    // do some transformations
    for (let contestAndGroup of this.enrolledContestsAndGroups) {
      if (contestAndGroup.group.leaderName === this.$store.state.username) {
        contestAndGroup.group.identity = '队长'
      } else {
        contestAndGroup.group.identity = '队员'
      }
    }
  },
  computed: {
    enrolledFinished: function() {
      let ret = []
      for (let contestAndGroup of this.enrolledContestsAndGroups) {
        if (contestAndGroup.contest.stage === -1) {
          ret.push(contestAndGroup)
        }
      }
      return ret
    },
    enrolledUnfinished: function() {
      let ret = []
      for (let contestAndGroup of this.enrolledContestsAndGroups) {
        if (contestAndGroup.contest.stage !== -1) {
          ret.push(contestAndGroup)
        }
      }
      return ret
    }
  },
  components: {
    'enrolled-contest-unfinished': EnrolledContestUnfinished,
    'enrolled-contest-finished': EnrolledContestFinished
  }
}
</script>

<style scoped>
.info-tag {
  color: #409eff;
  margin-left: 10px;
  margin-right: 10px;
}
</style>
