<template>
  <div>
    <el-row>
      <el-col :span="24">
        <el-steps :active="displayStage" align-center>
          <el-step v-for="(step,index) in displaySteps" :title="step.name" :description="step.desc" :key="index"></el-step>
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
export default {
  props: ['contest', 'contestId'],
  methods: {
    incCurrentStage() {
      this.$confirm('确认前往下一个阶段？')
        .then(() => {
          let nextStage = this.contest.stage + 1
          if (nextStage > this.procedure.slice(-1)[0].stage + 1) {
            nextStage = -1
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
              this.$alert(err)
            })
        })
        .catch(() => {})
    }
  },
  computed: {
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
          desc: '开始于' + step.startTime + '\n结束于' + step.endTime
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
  }
}
</script>

<style>
</style>
