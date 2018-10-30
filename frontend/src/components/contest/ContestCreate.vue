<template>
  <el-row align="middle" type="flex">
    <el-col :span="4"></el-col>
    <el-col :span="16">
      <el-form ref="form" :model="contest" label-width="80px">
        <el-form-item label="比赛名称">
          <el-input v-model="contest.name"></el-input>
        </el-form-item>
        <el-form-item label="比赛学科">
          <el-input v-model="contest.subject"></el-input>
        </el-form-item>
        <el-form-item label="报名时间">
          <el-col :span="11">
            <el-date-picker type="date" placeholder="选择日期" v-model="contest.enrollStartTime" style="width: 100%;"></el-date-picker>
          </el-col>
          <el-col class="line" :span="2">-</el-col>
          <el-col :span="11">
            <el-date-picker type="date" placeholder="选择时间" v-model="contest.enrollEndTime" style="width: 100%;"></el-date-picker>
          </el-col>
        </el-form-item>
        <el-col :span="12">
          <el-form-item label="队伍人数">
            <el-input-number v-model="contest.maxContestants" :min="1" :max="10"></el-input-number>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="报名费用">
            <el-input-number v-model="contest.charge" :min="1" :max="1000"></el-input-number>
          </el-form-item>
        </el-col>
        <el-form-item label="比赛描述">
          <el-input type="textarea" placeholder="请输入内容" :rows="10" v-model="contest.detail">
          </el-input>
        </el-form-item>
        <el-form-item label="报名网站">
          <el-col :span="6">
            使用本站提供的报名网站
            <el-checkbox v-model="useDefaultEnrollLink"></el-checkbox>
          </el-col>
          <el-col :span="6">若否，请输入报名网站链接</el-col>
          <el-col :span="6">
            <el-input v-model="contest.enrollUrl" :disabled="useDefaultEnrollLink" placeholder="请输入内容"></el-input>
          </el-col>
        </el-form-item>
        <el-form-item label="比赛流程">
          <el-input type="textarea" placeholder="请输入内容" :rows="10" v-model="contest.procedure">
          </el-input>
        </el-form-item>
        <el-form-item label="评分标准">
          <el-input type="textarea" placeholder="请输入内容" :rows="10" v-model="contest.judgingStandard">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleCreateContest">立即创建</el-button>
        </el-form-item>
      </el-form>
    </el-col>
    <el-col :span="4"></el-col>
  </el-row>
</template>
<script>
export default {
  name: 'ContestCreate',
  data() {
    return {
      useDefaultEnrollLink: false,
      contest: {
        name: null,
        subject: null,
        maxContestants: null,
        enrollStartTime: null,
        enrollEndTime: null,
        detail: null,
        procedure: null,
        enrollUrl: null,
        charge: null,
        judgingStandard: null,
        publisherName: null
      }
    }
  },
  methods: {
    handleCreateContest() {
      if (this.useDefaultEnrollLink) this.contest.enrollUrl = null
      let sd = new Date(this.contest.enrollStartTime)
      this.contest.enrollStartTime = sd.toISOString()
      let ed = new Date(this.contest.enrollEndTime)
      this.contest.enrollEndTime = ed.toISOString()
      this.$http
        .post(
          '/graphql',
          {
            query: `mutation{createCompetition(
              name:${this.contest.name},
              subject:${this.contest.subject},
              maxContestants:${this.contest.maxContestants},
              enrollStartTime:${this.contest.enrollStartTime},
              enrollEndTime:${this.contest.enrollEndTime},
              detail:${this.contest.detail},
              procedure:${this.contest.procedure},
              enrollUrl:${this.contest.enrollUrl},
              charge:${this.contest.charge},
              judgingStandard:${this.contest.judgingStandard},
              publisherName:"anonymous")
              {success}}`
          },
          {
            headers: {
              'X-CSRFToken': this.$cookies.get('csrftoken')
            },
            emulateJSON: true
          }
        )
        .then(function(response) {
          this.$router.push('/contest/list')
        })
    }
  }
}
</script>