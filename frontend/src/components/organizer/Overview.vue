<template>
  <div>
    <el-row>
      <el-col :span="12">
        <el-row>任务批阅进度: {{ stat.reviewedTasks }}/{{ stat.totalTasks }}</el-row>
        <el-row>
          <el-progress type="circle" :percentage="reviewPercentage"></el-progress>
        </el-row>
      </el-col>
      <el-col :span="12">
        <el-row>选手提交进度: {{ stat.submittedGroups }}/{{ stat.qualifiedGroups }}</el-row>
        <el-row>
          <el-progress type="circle" :percentage="submitPercentage"></el-progress>
        </el-row>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <el-steps :active="displayStage" align-center>
          <el-step
            v-for="(step,index) in displaySteps"
            :title="step.name"
            :description="step.desc"
            :key="index"
          ></el-step>
        </el-steps>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="4">
        <el-button type="warning" @click="incCurrentStage">前往下一个阶段</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { getPercentage, isNullStage } from '@/lib/util'
export default {
  props: ['contest', 'contestId'],
  data() {
    return {
      stat: {
        totalTasks: 0,
        reviewedTasks: 0,
        qualifiedGroups: 0,
        submittedGroups: 0,
        isAssigned: true // 是否之前一键分配过
      }
    }
  },
  methods: {
    getPercentage,
    incCurrentStage() {
      this.$confirm('确认前往下一个阶段？')
        .then(() => {
          let nextStage = this.contest.stage + 1
          if (nextStage > this.contest.procedure.slice(-1)[0].stage + 1) {
            nextStage = -1
          }
          if (this.contest.stage === -1) {
            this.$alert('比赛已经结束，不能继续推进')
            return
          }
          this.$http
            .post(`/api/contests/${this.contestId}`, {
              stage: nextStage
            })
            .then(resp => {
              if (resp.body.code !== 0) {
                throw new Error(resp.body.error)
              }
              this.$emit('refreshContest')
            })
            .catch(err => {
              this.$alert(err.toString())
            })
        })
        .catch(err => {
          if (err.toString() !== 'cancel') {
            this.$alert(err)
          }
        })
    },
    refreshStat() {
      this.$http
        .get(`/api/contests/${this.contestId}/taskstat`, {
          params: {
            stage: this.contest.stage
          }
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.stat = resp.body.data
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    }
  },
  computed: {
    reviewPercentage() {
      return this.getPercentage(this.stat.reviewedTasks, this.stat.totalTasks)
    },
    submitPercentage() {
      return this.getPercentage(this.stat.submittedGroups, this.stat.qualifiedGroups)
    },
    displayStage() {
      if (this.contest.stage === -1) {
        return this.displaySteps.length - 1
      } else {
        return this.contest.stage
      }
    },
    displaySteps() {
      let steps = []
      steps.push({
        name: '尚未开始',
        desc: ''
      })
      for (let step of this.contest.procedure) {
        steps.push({
          name: step.name,
          desc: '开始于' + step.startTime + ' 结束于' + step.endTime
        })
        steps.push({
          name: step.name + ' 评审',
          desc: ''
        })
      }
      steps.push({
        name: '比赛结束',
        desc: ''
      })
      return steps
    }
  },
  created() {
    if (this.contest.id !== -1 && !isNullStage(this.contest.stage)) {
      this.refreshStat()
    }
  },
  watch: {
    contest() {
      if (this.contest.id !== -1 && !isNullStage(this.contest.stage)) {
        this.refreshStat()
      }
    }
  }
}
</script>

<style>
</style>
