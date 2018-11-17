<template>
  <div>
    <el-card class="title-card" :body-style="{ padding: '0px' }">
      <el-row style="margin: 0px;">
        <el-col :span="4">
          <img :src="contestInfo.imgUrl" style="width: 100%;" />
        </el-col>
        <el-col :span="16" style="text-align: left;">
          <h1 style="margin: 10px; font-size: 32px; font-weight: bold;">{{contestInfo.name}}</h1>
          <div style="margin-left: 10px;">
            <span style="color: gray; margin-right: 5px;">比赛学科</span><span style="font-weight: bold; color: #409eff;">{{contestInfo.subject}}</span>
          </div>
          <div style="margin-left: 10px;">
            <span style="color: gray; margin-right: 5px;">主办单位</span><span style="font-weight: bold; color: #409eff;">{{contestInfo.publisher}}</span>
          </div>
          <div style="margin-left: 10px;">
            <span style="color: gray; margin-right: 5px;">队伍人数</span><span style="font-weight: bold; color: #409eff;">{{contestInfo.groupSize}}</span>
          </div>
        </el-col>
        <el-col :span="4" style="text-align: right;">
          <div style="margin-right: 20px;">
            <div style="margin-top: 10px; color: green; font-size: 24px;">{{contestInfo.upvote}} <i class="el-icon-arrow-up" /></div>
            <div style="margin-top: 10px; color: darkred; font-size: 24px;">{{contestInfo.downvote}} <i class="el-icon-arrow-down" /></div>
            <el-button-group style="margin-top: 15px;">
              <el-button style="color: green" @click="todoHandler">👍</el-button>
              <el-button style="color: darkred" @click="todoHandler">👎</el-button>
            </el-button-group>
          </div>
        </el-col>
      </el-row>
    </el-card>

    <h2 class="title">比赛流程</h2>
    <el-table :data="humanReadableProcedure" stripe style="width: 100%;">
      <el-table-column prop="name" label="名称"></el-table-column>
      <el-table-column prop="startTime" label="开始日期" width="400"></el-table-column>
      <el-table-column prop="endTime" label="结束日期" width="400"></el-table-column>
    </el-table>

    <h2 class="title">比赛详情</h2>
    <mavon-editor v-model="contestInfo.detail" :editable="false" :defaultOpen="'preview'" :subfield="false" :toolbarsFlag="false" />

    <h2 class="title">报名信息</h2>
    <div style="font-size: 20px;">
      <div>报名开始时间：<span style="font-weight: bold;">{{humanReadableEnrollStart}}</span></div>
      <div>报名结束时间：<span style="font-weight: bold;">{{humanReadableEnrollEnd}}</span></div>
      <div style="margin-top: 20px;">报名费用：{{contestInfo.charge}} 元</div>
    </div>

    <div style="margin-top: 20px;">
      <div v-if="beforeEnrollment">报名尚未开始</div>
      <div v-else-if="afterEnrollment">报名已经结束</div>
      <el-button v-else type="primary" @click="handleEnroll">点击此处报名</el-button>
    </div>
  </div>
</template>

<script>
import { isoToHumanReadable } from '@/lib/util.js'

export default {
  name: 'ContestDetail',
  async created() {
    let response = await this.$http.get(`/api/contests/${this.$route.params.id}`)
    if (response.body.code !== 0) {
      this.$message({ type: 'error', message: response.body.error })
      return
    }
    this.contestInfo = response.body.data
  },
  methods: {
    todoHandler() {
      alert('todo')
    },
    handleEnroll() {
      if (this.contestInfo.enrollUrl !== '') {
        this.$router.push(this.contestInfo.enrollUrl)
      } else {
        this.$router.push(`/contest/enroll/${this.contestInfo.id}`)
      }
    }
  },
  data() {
    return {
      contestInfo: null
    }
  },
  computed: {
    humanReadableProcedure() {
      let ret = []
      for (let step of this.contestInfo.procedure) {
        ret.push({
          name: step.name,
          startTime: isoToHumanReadable(step.startTime),
          endTime: isoToHumanReadable(step.endTime)
        })
      }

      return ret
    },
    humanReadableEnrollStart() {
      return isoToHumanReadable(this.contestInfo.enrollStart)
    },
    humanReadableEnrollEnd() {
      return isoToHumanReadable(this.contestInfo.enrollEnd)
    },
    beforeEnrollment() {
      return Date.now() < Date.parse(this.contestInfo.enrollStart)
    },
    afterEnrollment() {
      return Date.now() > Date.parse(this.contestInfo.enrollEnd)
    },
    enrollable() {
      return !this.beforeEnrollment && !this.afterEnrollment
    }
  }
}
</script>

<style scoped>
.title-card {
  height: 150px;
}

.title {
  font-size: 48px;
}
</style>
