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
        <el-steps :active="procedureActiveNum" finish-status="success" :align-center="true">
          <el-step :title="value.name" v-for="(value, index) in jsonProcedure" :key="index">{{ value.name }}</el-step>
        </el-steps>
        <el-row>
          <el-button type="primary"><a :href="contest.enrollUrl">立即报名</a></el-button>
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
          <el-col :span="12">{{ contest.maxContestants }}</el-col>
        </el-row>
        <el-row type="flex" align="middle">
          <el-col :span="12" class="my-title">
            报名开始时间
          </el-col>
          <el-col :span="12">{{ contest.enrollStartTime }}</el-col>
        </el-row>
        <el-row type="flex" align="middle">
          <el-col :span="12" class="my-title">
            报名结束时间
          </el-col>
          <el-col :span="12">{{ contest.enrollStartTime }}</el-col>
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
      jsonProcedure: [],
      procedureActiveNum: -1,
      contest: {
        id: 0,
        name: '',
        subject: '',
        maxContestants: 0,
        enrollStartTime: null,
        enrollEndTime: null,
        detail: null,
        procedure: null,
        enrollUrl: null,
        charge: 0,
        numUpvote: null,
        numDownvote: null,
        judgingStandard: null
      }
    }
  },
  methods: {},
  created: function() {
    let self = this
    this.$http
      .post(
        '/graphql',
        {
          query: `query{competitionById(
            competitionId:${this.$route.params.id})
            {id,name,subject,maxContestants,enrollStartTime,enrollEndTime,detail,procedure,enrollUrl,charge,numUpvote,numDownvote,judgingStandard}}`
        },
        {
          headers: {
            'X-CSRFToken': this.$cookies.get('csrftoken')
          },
          emulateJSON: true
        }
      )
      .then(function(response) {
        self.contest = response.body.data.competitionById
        let sd = new Date(self.contest.enrollStartTime)
        let ed = new Date(self.contest.enrollEndTime)
        self.contest.enrollStartTime = formatDate(sd)
        self.contest.enrollEndTime = formatDate(ed)
        self.jsonProcedure = JSON.parse(self.contest.procedure)
        console.log(self.jsonProcedure)
        for (let i = 0; i < self.jsonProcedure.length; i++) {
          let prod = self.jsonProcedure[i]
          let myProd = {
            name: prod.name,
            startTime: new Date(prod.startTime),
            endTime: new Date(prod.endTime)
          }
          self.procedureList.push(myProd)
        }
        for (let i = 0; i < self.procedureList.length; i++) {
          let ed = self.procedureList[i].endTime
          let cd = new Date()
          if (cd <= ed) {
            self.procedureActiveNum = i
            break
          }
        }
        if (self.procedureActiveNum == -1) self.procedureActiveNum = self.procedureList.length
      })
  }
}
</script>