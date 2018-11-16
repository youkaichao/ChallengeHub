<template>
  <el-card :body-style="{ padding: '0px' }" class="single-card">
    <el-row style="margin: 0px;">
      <el-col :span="4">
        <img :src="contest.imgUrl" class="enrolled-contest-card" />
      </el-col>
      <el-col :span="12" style="text-align: left; padding-left: 20px;">
        <div class="contest-name"> {{ contest.name }} </div>
        <div class="contest-info"> {{ contest.publisher }} </div>
        <div class="contest-info"> 比赛已结束于 {{ endingDeadline }} </div>
        <el-button type="text" @click="$router.push(`/contest/detail/${contest.id}`)">查看比赛详情</el-button>
      </el-col>
      <el-col :span="8" style="text-align: right; padding-right: 20px;">
        <div class="group-name">
          {{ group.name }}{{ group.identity }}
        </div>
        <div class="contest-result">
          你的名次：<b>{{ group.rank }}</b>
        </div>
        <div style="margin-top: 20px;">
          <el-button type="primary" plain @click="todoHandler()">下载作品</el-button>
          <el-button type="primary" @click="todoHandler()">查看结果详情</el-button>
        </div>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
import { isoToHumanReadable } from '@/lib/util.js'

export default {
  name: 'EnrolledContestFinished',
  computed: {
    endingDeadline: function() {
      let procedure = this.contest.procedure
      let deadline = procedure[procedure.length - 1].endTime
      return isoToHumanReadable(deadline)
    }
  },
  props: ['contest', 'group'],
  methods: {
    todoHandler: function() {
      // TODO
      alert('todo')
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

.contest-result {
  margin-top: 5px;
  color: gray;
}
</style>
