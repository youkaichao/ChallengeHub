<template>
  <el-row>
    <el-row>
      <el-input
        placeholder="请输入比赛名"
        v-model="searchInput"
        style="width: 500px;"
      >
        <el-button
          slot="append"
          icon="el-icon-search"
          @click="handleSearch"
        ></el-button>
      </el-input>
    </el-row>
    <el-row>
      <el-alert
        title="然而并没有数据"
        type="warning"
        center
        style="width: 600px; margin: auto; margin-top: 30px;"
        show-icon
        v-if="contestListEmpty"
      >
      </el-alert>
      <contest-burge
        style="margin-top: 20px;"
        v-on:detail-on-click="routeToDetail"
        v-for="contestInfo in allContestInfo"
        v-bind:contestInfo="contestInfo"
        v-bind:key="contestInfo.contestId"
      ></contest-burge>
    </el-row>
  </el-row>
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
    },
    handleSearch: async function() {
      let response = await this.$http.get('/api/contests', {
        params: { search: this.searchInput }
      })
      this.allContestInfo = response.body.data
    }
  },
  async created() {
    let response = await this.$http.get('/api/contests')
    this.allContestInfo = response.body.data
  },
  computed: {
    contestListEmpty() {
      return this.allContestInfo.length === 0
    }
  }
}
</script>

<style>
</style>
