<template>
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
            <el-button style="color: green">👍</el-button>
            <el-button style="color: darkred">👎</el-button>
          </el-button-group>
        </div>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
export default {
  name: 'ContestBanner',
  props: ['contestInfo']
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
