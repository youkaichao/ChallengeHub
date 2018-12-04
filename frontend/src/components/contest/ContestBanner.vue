<template>
  <el-card
    class="title-card"
    :body-style="{ padding: '0px' }"
  >
    <el-row style="margin: 0px;">
      <el-col :span="4">
        <img
          :src="contestInfo.imgUrl"
          style="width: 100%;"
        />
      </el-col>
      <el-col
        :span="16"
        style="text-align: left;"
      >
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
      <el-col
        :span="4"
        style="text-align: right;"
      >
        <div style="margin-right: 20px;">
          <div style="margin-top: 10px; color: green; font-size: 24px;">{{upvote}} <i class="el-icon-arrow-up" /></div>
          <div style="margin-top: 10px; color: darkred; font-size: 24px;">{{downvote}} <i class="el-icon-arrow-down" /></div>
          <el-button-group style="margin-top: 15px;">
            <el-button @click="handleUpvote()">
              <font-awesome-icon
                style="color: green;"
                :icon="upvoteIcon"
                size="lg"
              />
            </el-button>
            <el-button @click="handleDownvote()">
              <font-awesome-icon
                style="color: darkred;"
                :icon="downvoteIcon"
                size="lg"
              />
            </el-button>
          </el-button-group>
        </div>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
export default {
  name: 'ContestBanner',
  props: ['contestInfo'],
  data() {
    return {
      upvote: 0,
      downvote: 0,
      upvoteStatus: 0
    }
  },
  methods: {
    async handleUpvote() {
      if(!this.$store.state.login){
        this.$message({
          message: '登陆以评价比赛',
          type: 'warning'
        });
        return
      }
      let response = await this.$http.post(`/api/contests/${this.contestInfo.id}/vote`, { upvote: 1 })
      this.refreshVotes(response)
    },
    async handleDownvote() {
      let response = await this.$http.post(`/api/contests/${this.contestInfo.id}/vote`, { upvote: -1 })
      this.refreshVotes(response)
    },
    refreshVotes(response) {
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }

      this.upvote = response.body.data.upvote
      this.downvote = response.body.data.downvote
      this.upvoteStatus = response.body.data.upvoteStatus
    }
  },
  computed: {
    upvoteIcon() {
      if (this.upvoteStatus === 1) {
        return ['fas', 'thumbs-up']
      } else {
        return ['far', 'thumbs-up']
      }
    },
    downvoteIcon() {
      if (this.upvoteStatus === -1) {
        return ['fas', 'thumbs-down']
      } else {
        return ['far', 'thumbs-down']
      }
    }
  },
  created() {
    let upvoteStatus = this.contestInfo.userRelated.upvoteStatus
    this.upvote = this.contestInfo.upvote
    this.downvote = this.contestInfo.downvote
    if (upvoteStatus === null || upvoteStatus === undefined) {
      return
    }
    this.upvoteStatus = upvoteStatus
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
