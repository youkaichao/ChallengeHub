<template>
  <div>
    <contest-banner :contestInfo="contestInfo" />

    <h2 class="title">比赛流程</h2>
    <el-table
      :data="humanReadableProcedure"
      stripe
      style="width: 100%;"
    >
      <el-table-column
        prop="name"
        label="名称"
      ></el-table-column>
      <el-table-column
        prop="startTime"
        label="开始日期"
        width="400"
      ></el-table-column>
      <el-table-column
        prop="endTime"
        label="结束日期"
        width="400"
      ></el-table-column>
    </el-table>

    <h2 class="title">报名信息</h2>
    <div style="font-size: 20px;">
      <div>报名开始时间：<span style="font-weight: bold;">{{humanReadableEnrollStart}}</span></div>
      <div>报名结束时间：<span style="font-weight: bold;">{{humanReadableEnrollEnd}}</span></div>
      <div style="margin-top: 20px;">报名费用：{{contestInfo.charge}} 元</div>
    </div>

    <div style="margin-top: 20px;">
      <div v-if="beforeEnrollment">报名尚未开始</div>
      <div v-else-if="afterEnrollment">报名已经结束</div>
      <el-button
        v-else
        type="primary"
        @click="handleEnroll"
      >点击此处以组长身份报名</el-button>
    </div>

    <div v-if="this.contestInfo.enrollUrl === ''">
    <el-button
      type="primary"
      style="margin-top: 20px;"
      @click="$router.push(`/contest/notice/${contestInfo.id}`)"
    >比赛公告</el-button>
    <el-button
      type="primary"
      @click="gotoGroupList"
    >
      查看已报名的队伍
    </el-button>
    </div>

    <h2 class="title">比赛详情</h2>
    <mavon-editor
      v-model="contestInfo.detail"
      :editable="false"
      :defaultOpen="'preview'"
      :subfield="false"
      :toolbarsFlag="false"
    />
  </div>
</template>

<script>
import { isoToHumanReadable } from '@/lib/util.js'
import ContestBanner from './ContestBanner.vue'

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
    gotoGroupList() {
      this.$router.push({
        name: 'grouplist',
        params: {
          id: this.contestInfo.id
        }
      })
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
      contestInfo: {
        id: -1,
        name: '',
        subject: '',
        groupSize: 0,
        enrollStart: '',
        enrollEnd: '',
        imgUrl: '',
        enrollUrl: '',
        charge: 0,
        upvote: 0,
        downvote: 0,
        publisher: '',
        stage: 0,
        procedure: [],
        detail: '',
        userRelated: {
          upvoteStatus: 0
        }
      }
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
  },
  components: {
    'contest-banner': ContestBanner
  }
}
</script>

<style scoped>
.title {
  font-size: 48px;
}
</style>
