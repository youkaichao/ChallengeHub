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
        <el-row>
          <el-button type="primary">立即报名</el-button>
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
export default {
  name: 'ContestDetail',
  data() {
    return {
      contest: {
        id: null,
        name: null,
        subject: null,
        maxContestants: null,
        enrollStartTime: null,
        enrollEndTime: null,
        detail: null,
        procedure: null,
        enrollUrl: null,
        charge: null,
        numUpvote: null,
        numDownvote: null,
        judgingStandard: null
      }
    }
  },
  methods: {},
  created: function() {
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
        console.log(response)
        this.contest = response.body.data.competitionById
        let sd = new Date(this.contest.enrollStartTime)
        let ed = new Date(this.contest.enrollEndTime)
        this.contest.enrollStartTime = `${sd.getFullYear()}年${sd.getMonth() + 1}月${sd.getDate()}日`
        this.contest.enrollEndTime = `${ed.getFullYear()}年${ed.getMonth() + 1}月${ed.getDate()}日`
      })
  }
}
</script>