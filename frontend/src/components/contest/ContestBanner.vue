<template>
  <el-card
    class="title-card"
    :body-style="{ padding: '0px' }"
  >
    <el-row style="margin: 0px;">
      <el-col :span="4">
        <img
          :src="contestInfo.imgUrl"
          class="fix-img"
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
          <div style="margin-top: 10px; color: green; font-size: 24px;">{{contestInfo.upvote}} <i class="el-icon-arrow-up" /></div>
          <div style="margin-top: 10px; color: darkred; font-size: 24px;">{{contestInfo.downvote}} <i class="el-icon-arrow-down" /></div>
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
    return {}
  },
  methods: {
    async handleUpvote() {
      if(this.loginCheck() === false) return;
      let response = await this.$http.post(`/api/contests/${this.contestInfo.id}/vote`, { upvote: 1 })
      this.refreshVotes(response)
    },
    async handleDownvote() {
      if(this.loginCheck() === false) return;
      let response = await this.$http.post(`/api/contests/${this.contestInfo.id}/vote`, { upvote: -1 })
      this.refreshVotes(response)
    },
    refreshVotes(response) {
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }

      this.contestInfo.upvote = response.body.data.upvote
      this.contestInfo.downvote = response.body.data.downvote
      this.contestInfo.userRelated.upvoteStatus = response.body.data.upvoteStatus
    },
    loginCheck() {
      if (!this.$store.state.login) {
        this.$message({
          message: '登录以评价比赛',
          type: 'warning'
        })
        return false
      }
      return true
    }
  },
  computed: {
    upvoteIcon() {
      if (this.contestInfo.userRelated.upvoteStatus === 1) {
        return ['fas', 'thumbs-up']
      } else {
        return ['far', 'thumbs-up']
      }
    },
    downvoteIcon() {
      if (this.contestInfo.userRelated.upvoteStatus === -1) {
        return ['fas', 'thumbs-down']
      } else {
        return ['far', 'thumbs-down']
      }
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

.fix-img {
  max-width: 200px;
  max-height: 152px;
  width: auto;
  height: auto;
}
</style>
