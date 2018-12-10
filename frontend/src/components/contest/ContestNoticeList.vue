<template>
  <div>
    <contest-banner :contestInfo="contestInfo"/>
    <h1 style="font-size: 40px;">
      <span style="margin-right: 20px; font-weight: bold;">{{contestInfo.name}}</span>
      <span style="color: #409eff">公告列表</span>
    </h1>

    <el-alert
      v-if="notices.length === 0"
      title="然而并没有数据"
      type="warning"
      center
      style="width: 600px; margin: auto;"
      show-icon
    ></el-alert>
    <notice-burger
      style="margin-top: 10px; width: 800px; margin-left: auto; margin-right: auto;"
      v-for="(notice, index) of notices"
      :key="index"
      :notice="notice"
      :competitionId="contestId"
    />
  </div>
</template>

<script>
import NoticeBurger from './NoticeBurger.vue'
import ContestBanner from './ContestBanner.vue'

export default {
  name: 'ContestNoticeList',
  data() {
    return {
      contestId: null,
      notices: [],
      contestInfo: null
    }
  },
  async created() {
    this.contestId = this.$route.params.id
    let response = await this.$http.get(`/api/contests/${this.contestId}/notices`)
    if (response.body.code !== 0) {
      this.$message({ type: 'error', message: response.body.error })
      return
    }
    this.notices = response.body.data.notices
    this.contestInfo = response.body.data.contest
  },
  components: {
    'notice-burger': NoticeBurger,
    'contest-banner': ContestBanner
  }
}
</script>

<style scoped>
</style>
