<template>
  <el-card :body-style="{ padding: '0px' }" class="single-card">
    <el-row style="margin: 0px;">
      <el-col :span="4">
        <img :src="contest.imgUrl" class="enrolled-contest-card" />
      </el-col>
      <el-col :span="12" style="text-align: left; padding-left: 20px;">
        <div class="contest-name"> {{ contest.name }} </div>
        <div class="contest-info"> {{ contest.publisher }} </div>
        <div class="contest-info"> 当前阶段 <b>{{ currentStage }}</b> 结束于 <b>{{ currentDeadline }}</b></div>
        <el-button type="text" @click="$router.push(`/contest/detail/${contest.id}`)">查看比赛详情</el-button>
      </el-col>
      <el-col :span="8" style="text-align: right; padding-right: 20px;">
        <div class="group-name">
          <span> {{ group.name }}{{ group.identity }} </span>
        </div>
        <div class="commit-status">
          <span> {{ group.hasCommit ? "作品已提交" : "作品未提交！" }} </span>
        </div>
        <el-button type="primary" @click="todoHandler()" v-show="!group.hasCommit" class="commit-button">提交作品</el-button>
        <el-button type="primary" @click="todoHandler()" v-show="group.hasCommit" class="commit-button" plain>修改作品</el-button>
        <el-button type="primary" @click="todoHandler()" v-show="group.hasCommit" class="commit-button" plain>下载作品</el-button>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
import { isoToHumanReadable } from '@/lib/util.js'

export default {
  name: 'EnrolledContestUnfinished',
  methods: {
    todoHandler: function() {
      alert('todo')
    }
  },
  props: ['contest', 'group'],
  computed: {
    currentStage: function() {
      let stageIndex = this.contest.stage
      return JSON.parse(this.contest.procedure)[stageIndex].name
    },
    currentDeadline: function() {
      let stageIndex = this.contest.stage
      return isoToHumanReadable(JSON.parse(this.contest.procedure)[stageIndex].endTime)
    }
  }
}
</script>

<style scoped>
.single-card {
  height: 150px;
}

.enrolled-contest-card {
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

.group-name {
  margin-top: 10px;
  font-weight: bold;
  font-size: 24px;
}

.commit-status {
  margin-top: 5px;
  color: gray;
}

.commit-button {
  margin-top: 20px;
}
</style>
