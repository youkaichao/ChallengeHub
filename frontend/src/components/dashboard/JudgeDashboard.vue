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
          <h1 style="font-size: 48px; margin: 0">我评审的比赛</h1>
        </el-col>
        <el-col :span="6" style="text-align: right; margin: auto;">
          <el-button type="primary" plain @click="$emit('switch-competitor')">切换到选手视图</el-button>
        </el-col>
      </el-row>
    </div>
    <el-tabs>
      <el-tab-pane label="未结束的比赛">
        <el-alert
          v-if="judgeUnfinished.length === 0"
          title="然而并没有数据"
          type="warning"
          center
          style="width: 600px; margin: auto;"
          show-icon
        ></el-alert>
        <judged-contest-unfinished style="margin-top: 10px;" v-for="info of judgeUnfinished" :contest="info.contest" :task="info.task" :key="info.contest.id" />
      </el-tab-pane>
      <el-tab-pane label="已结束的比赛">
        <el-alert
          v-if="judgeFinished.length === 0"
          title="然而并没有数据"
          type="warning"
          center
          style="width: 600px; margin: auto;"
          show-icon
        ></el-alert>
        <judged-contest-finished style="margin-top: 10px;" v-for="info of judgeFinished" :contest="info.contest" :task="info.task" :key="info.contest.id" />
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import JudgedConetestUnfinished from './JudgedContestUnfinished.vue'
import JudgedConetestFinished from './JudgedContestFinished.vue'

export default {
  name: 'JudgeDashboard',
  data() {
    return {
      judgedContestAndTasks: []
    }
  },
  async created() {
    let response = await this.$http.get('/api/users/judged')
    if (response.body.code !== 0) {
      this.$message({type: 'error', message: response.body.error})
      return
    }
    this.judgedContestAndTasks = response.body.data
  },
  computed: {
    judgeFinished: function() {
      let ret = []
      for (let contestAndTask of this.judgedContestAndTasks) {
        if (contestAndTask.contest.stage === -1) {
          ret.push(contestAndTask)
        }
      }
      return ret
    },
    judgeUnfinished: function() {
      let ret = []
      for (let contestAndTask of this.judgedContestAndTasks) {
        if (contestAndTask.contest.stage !== -1) {
          ret.push(contestAndTask)
        }
      }
      return ret
    }
  },
  components: {
    'judged-contest-unfinished': JudgedConetestUnfinished,
    'judged-contest-finished': JudgedConetestFinished
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
