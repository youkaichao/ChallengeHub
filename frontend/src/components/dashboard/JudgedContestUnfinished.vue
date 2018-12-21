<template>
  <el-card :body-style="{ padding: '0px' }" class="single-card">
    <el-row style="margin: 0px;">
      <el-col :span="4">
        <img :src="contest.imgUrl" class="judged-contest-card" />
      </el-col>
      <el-col :span="16" style="text-align: left; padding-left: 20px;">
        <div class="contest-name"> {{ contest.name }} </div>
        <div class="contest-info"> {{ contest.publisher }} </div>
        <div class="contest-info" v-if="contest.stage === 0">比赛尚未开始</div>
        <div class="contest-info" v-if="isJudgeStage">阶段 <b>{{ currentStage }}</b> 评审结束于 <b>{{ currentDeadline }}</b></div>
        <div class="contest-info" v-if="contest.stage !== 0 && !isJudgeStage">阶段 <b> {{ currentStage }} </b>评审开始于 <b>{{ currentDeadline }}</b></div>
        <el-button type="text" @click="$router.push(`/contest/detail/${contest.id}`)">比赛详情</el-button>
        <el-button type="text" @click="$router.push(`/contest/notice/${contest.id}`)">比赛公告</el-button>
      </el-col>

      <el-col :span="4" style="text-align: right; padding-right: 20px; ">
        <div class="judging-status" v-html="judgingStatus"></div>
        <el-progress v-if="isJudgeStage" style="margin-top: 15px;" :percentage="task.count === 0 ? 1.0 : parseFloat((task.done * 100 / task.count).toFixed(1))" :text-inside="true" :stroke-width="18"></el-progress>
        <el-progress v-if="!isJudgeStage" style="margin-top: 15px; visibility: hidden;" :percentage="0" :text-inside="true" :stroke-width="18"></el-progress>
        <el-button v-if="!isJudgeStage" style="margin-top: 20px;" type="primary" plain @click="gotoWorkspace()">查看评审</el-button>
        <el-button v-if="isJudgeStage && (!judgeCompelete)" style="margin-top: 20px;" type="primary" @click="gotoWorkspace()">进行评审</el-button>
        <el-button v-if="isJudgeStage && judgeCompelete" style="margin-top: 20px;" type="primary" plain @click="gotoWorkspace()">修改评审</el-button>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
import { isoToHumanReadable } from '@/lib/util.js'

export default {
  name: 'JudgedContestUnfinished',
  methods: {
    todoHandler: function() {
      // TODO
      alert('todo')
    },
    gotoWorkspace() {
      this.$router.push(`judge/workspace/${this.contest.id}`)
    }
  },
  props: ['contest', 'task'],
  computed: {
    isJudgeStage: function() {
      let currentStage = this.contest.stage
      if (currentStage > 0 && currentStage % 2 === 0) return true
      return false
    },
    currentStage: function() {
      let stageIndex = this.contest.stage
      if (stageIndex % 2 === 0) return this.contest.procedure[stageIndex / 2 - 1].name
      else return this.contest.procedure[(stageIndex - 1) / 2].name
    },
    currentDeadline: function() {
      let stageIndex = this.contest.stage
      let procedure = this.contest.procedure
      if (stageIndex % 2 === 0 && stageIndex !== procedure.length * 2) return isoToHumanReadable(procedure[stageIndex / 2].startTime)
      else if (stageIndex % 2 === 0) return '主办方规定的时间'
      else return isoToHumanReadable(this.contest.procedure[(stageIndex - 1) / 2].endTime)
    },
    judgeCompelete: function() {
      return this.task.count === this.task.done
    },
    judgingStatus() {
      if (!this.isJudgeStage) return '<span style="color: gray;">无评审任务</span>'
      if (this.task.count === this.task.done) return '<span style="color: gray;">评审任务完成</span>'
      return '评审进行中'
    }
  }
}
</script>

<style scoped>
.single-card {
  height: 150px;
}

.judged-contest-card {
  max-width: 200px;
  max-height: 152px;
  width: auto;
  height: auto;
}

.contest-name {
  margin-top: 10px;
  font-weight: bold;
  font-size: 32px;
}

.contest-info {
  margin-top: 5px;
  color: grey;
}

.judging-status {
  margin-top: 10px;
  font-weight: bold;
  font-size: 24px;
}
</style>
