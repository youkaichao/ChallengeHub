<template>
  <div>
    <el-input placeholder="请输入比赛名" v-model="searchInput" style="width: 500px;">
      <el-button slot="append" icon="el-icon-search"></el-button>
    </el-input>
    <contest-burge style="margin-top: 20px;" v-on:detail-on-click="routeToDetail" v-for="contestInfo in allContestInfo" v-bind:contestInfo="contestInfo" v-bind:key="contestInfo.contestId"></contest-burge>
  </div>
</template>

<script>
import ContestBurge from './ContestBurge.vue'
export default {
  name: 'ContestAllList',
  components: {
    'contest-burge': ContestBurge
  },
  data() {
    return {
      allContestInfo: [],
      searchInput: ''
    }
  },
  methods: {
    routeToDetail: function(contestId) {
      this.$router.push(`/contest/detail/${contestId}`)
    }
  },
  async created() {
    let response = await this.$http.get('/api/contests')
    this.allContestInfo = response.body.data
  }
}
</script>

<style>
</style>
