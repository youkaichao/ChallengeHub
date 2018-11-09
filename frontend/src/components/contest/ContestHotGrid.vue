<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="6">
        <contest-card v-if="showCard[0]" v-on:detail-on-click="routeToDetail" v-bind:contestInfo="contestsInfo[0]"></contest-card>
      </el-col>
      <el-col :span="6">
        <contest-card v-if="showCard[1]" v-on:detail-on-click="routeToDetail" v-bind:contestInfo="contestsInfo[1]"></contest-card>
      </el-col>
      <el-col :span="6">
        <contest-card v-if="showCard[2]" v-on:detail-on-click="routeToDetail" v-bind:contestInfo="contestsInfo[2]"></contest-card>
      </el-col>
      <el-col :span="6">
        <contest-card v-if="showCard[3]" v-on:detail-on-click="routeToDetail" v-bind:contestInfo="contestsInfo[3]"></contest-card>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="6">
        <contest-card v-if="showCard[4]" v-on:detail-on-click="routeToDetail" v-bind:contestInfo="contestsInfo[4]"></contest-card>
      </el-col>
      <el-col :span="6">
        <contest-card v-if="showCard[5]" v-on:detail-on-click="routeToDetail" v-bind:contestInfo="contestsInfo[5]"></contest-card>
      </el-col>
      <el-col :span="6">
        <contest-card v-if="showCard[6]" v-on:detail-on-click="routeToDetail" v-bind:contestInfo="contestsInfo[6]"></contest-card>
      </el-col>
      <el-col :span="6">
        <contest-card v-if="showCard[7]" v-on:detail-on-click="routeToDetail" v-bind:contestInfo="contestsInfo[7]"></contest-card>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="6">
        <contest-card v-if="showCard[8]" v-on:detail-on-click="routeToDetail" v-bind:contestInfo="contestsInfo[8]"></contest-card>
      </el-col>
      <el-col :span="6">
        <contest-card v-if="showCard[9]" v-on:detail-on-click="routeToDetail" v-bind:contestInfo="contestsInfo[9]"></contest-card>
      </el-col>
      <el-col :span="6">
        <contest-card v-if="showCard[10]" v-on:detail-on-click="routeToDetail" v-bind:contestInfo="contestsInfo[10]"></contest-card>
      </el-col>
      <el-col :span="6">
        <contest-card v-if="showCard[11]" v-on:detail-on-click="routeToDetail" v-bind:contestInfo="contestsInfo[11]"></contest-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import ContestCard from './ContestCard.vue'

export default {
  name: 'ContestHotGrid',
  components: {
    'contest-card': ContestCard
  },
  async created() {
    let response = await this.$http.get('/api/contests', {
      params: { sortBy: 'numVotes' }
    })
    this.contestsInfo = response.body.data
  },
  data: function() {
    return {
      contestsInfo: []
    }
  },
  methods: {
    routeToDetail: function(contestId) {
      this.$router.push(`/contest/detail/${contestId}`)
    }
  },
  computed: {
    showCard: function() {
      let x = [...Array(12)].map((_, __) => false)
      for (let i = 0; i < Math.min(this.contestsInfo.length, 12); i++) {
        x[i] = true
      }
      return x
    }
  }
}
</script>
