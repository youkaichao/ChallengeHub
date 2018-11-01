<template>
  <el-row>
    <el-row :gutter="50">
      <el-col :span="18">
        <el-row>
          <h1>{{ contest.name }}</h1>
        </el-row>
        <el-row class="my-title">
          <h2>比赛详情</h2>
        </el-row>
        <hr />
        <el-row>
          <p>{{ contest.detail }}</p>
        </el-row>
        <el-row class="my-title">
          <h2>比赛流程</h2>
        </el-row>
        <hr />
        <el-steps :active="procedureActive" finish-status="success" :align-center="true">
          <el-step :title="value.name" v-for="(value, index) in procedureList" :key="index">{{ value.name }}</el-step>
        </el-steps>
        <el-row>
          <el-button type="primary"><a :href="contest.url">立即报名</a></el-button>
        </el-row>
      </el-col>
      <el-col :span="6">
        <el-row type="flex" align="middle">
          <el-col :span="12" class="my-title">
            比赛学科
          </el-col>
          <el-col :span="12">{{ contest.subject }}</el-col>
        </el-row>
        <el-row type="flex" align="middle">
          <el-col :span="12" class="my-title">
            队伍人数上限
          </el-col>
          <el-col :span="12">{{ contest.groupSize }}</el-col>
        </el-row>
        <el-row type="flex" align="middle">
          <el-col :span="12" class="my-title">
            报名开始时间
          </el-col>
          <el-col :span="12">{{ contest.enrollStart }}</el-col>
        </el-row>
        <el-row type="flex" align="middle">
          <el-col :span="12" class="my-title">
            报名结束时间
          </el-col>
          <el-col :span="12">{{ contest.enrollStart }}</el-col>
        </el-row>
        <el-row type="flex" align="middle">
          <el-col :span="12" class="my-title">
            报名费用
          </el-col>
          <el-col :span="12">{{ contest.charge }}元</el-col>
        </el-row>
      </el-col>
    </el-row>
  </el-row>
</template>
<script>
import { formatDate } from '#/js/util.js'
export default {
  name: 'ContestDetail',
  data() {
    return {
      procedureList: [],
      procedureActive: -1,
      contest: {
        name: null,
        subject: null,
        groupSize: null,
        enrollStart: null,
        enrollEnd: null,
        detail: null,
        procedure: null,
        url: null,
        charge: 0,
        upvote: null,
        downvote: null,
        publisher: null
      }
    }
  },
  created: function() {
    let self = this
    this.$http.get('/api/contest', { params: { id: this.$route.params.id } }, { emulateJSON: true }).then(function(response) {
      self.contest = response.body.data
      self.procedureList = JSON.parse(self.contest.procedure)
      console.log(self.procedureList)
      for (let i = 0; i < self.procedureList.length; i++) {
        let prod = self.procedureList[i],
          endTime = new Date(prod.endTime)
        console.log(endTime, i)
        if (new Date() <= endTime) {
          self.procedureActive = i
          break
        }
      }
      console.log(self.procedureActive)
      if (self.procedureActive == -1) self.procedureActive = self.procedureList.length
      console.log(self.procedureActive)
    })
  }
}
</script>