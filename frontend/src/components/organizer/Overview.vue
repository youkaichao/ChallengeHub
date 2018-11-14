<template>
  <div>
    <el-row>
      <el-col :span="24">
        <el-steps :active="displayStage" align-center>
          <el-step v-for="(step,index) in procedureList" :title="step.name" :description="step.startTime" :key="index"></el-step>
        </el-steps>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="4">
        <el-button type="primary" @click="addCurrentStage(1)">前往下一个进度</el-button>
      </el-col>
      <el-col :span="4" :offset="1">
        <el-button type="primary" @click="addCurrentStage(-1)">回到上一个进度</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  props: ['contest', 'procedureList', 'contestId'],
  methods: {
    addCurrentStage(direction) {
      if (direction !== 1 && direction !== -1) {
        // console.warn('invalid direction!')
        return
      }
      let nextStage = this.currentStage + direction
      if (direction === 1 && this.currentStage === -1) {
        return
      } else if (direction === -1 && this.currentStage === 0) {
        return
      } else if (direction === 1 && this.currentStage === this.procedureList.length) {
        nextStage = -1
      } else if (direction === -1 && this.currentStage === -1) {
        nextStage = this.procedureList.length
      }
      this.$http
        .post(`/api/contests/${this.contestId}`, {
          stage: nextStage
        })
        .then(
          () => {
            this.$emit('refreshContest')
          },
          () => {
            // console.warn('addCurrentStage failed!')
          }
        )
    }
  },
  computed: {
    displayStage() {
      if (this.currentStage === -1) {
        return this.procedureList.length
      } else {
        return this.currentStage - 1
      }
    },
    currentStage() {
      if (this.contest) {
        return this.contest.stage
      } else {
        return 0
      }
    }
  }
}
</script>

<style>
</style>
