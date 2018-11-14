<template>
  <el-card :body-style="{ padding: '0px' }" class="single-card">
    <el-row style="margin: 0px;">
      <el-col :span="4">
        <img :src="contest.imgUrl" class="judged-contest-card" />
      </el-col>
      <el-col :span="16" style="text-align: left; padding-left: 20px;">
        <div class="contest-name"> {{ contest.name }} </div>
        <div class="contest-info"> {{ contest.publisher }} </div>
        <div class="contest-info"> 当前阶段 <b>{{ currentStage }}</b> 结束于 <b>{{ currentDeadline }}</b></div>
        <el-button type="text" @click="$router.push(`/contest/detail/${contest.id}`)">查看比赛详情</el-button>
      </el-col>

      <el-col :span="4" style="text-align: right; padding-right: 20px; ">
        <div class="judging-status"> {{ task.count === task.done ? "评审任务完成" : "评审进行中" }} </div>
        <el-progress style="margin-top: 15px;" :percentage="(task.done * 100 / task.count).toFixed(1)" :text-inside="true" :stroke-width="18"></el-progress>
        <el-button v-if="!judgeCompelete" style="margin-top: 20px;" type="primary" @click="todoHandler()">进行评审</el-button>
        <el-button v-if="judgeCompelete" style="margin-top: 20px;" type="primary" plain @click="todoHandler()">修改评审</el-button>
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
    }
  },
  props: ['contest', 'task'],
  computed: {
    currentStage: function() {
      let stageIndex = this.contest.stage
      return JSON.parse(this.contest.procedure)[stageIndex].name
    },
    currentDeadline: function() {
      let stageIndex = this.contest.stage
      return isoToHumanReadable(JSON.parse(this.contest.procedure)[stageIndex].endTime)
    },
    judgeCompelete: function() {
      return this.task.count === this.task.done
    }
  }
}
</script>

<style scoped>
.single-card {
  height: 150px;
}

.judged-contest-card {
  width: 100%;
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
