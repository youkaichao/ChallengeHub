<template>
  <el-card :body-style="{ padding: '0px' }">
    <img :src="contestInfo.imgUrl" style="width: 100%; display: block" />
    <div style="padding 14px">
      <div class="left-align" style="padding-top: 5px;">
        {{ contestInfo.name }}
      </div>
      <div class="deadline left-align">报名截止于 {{ enrollEndHumanReadable }}</div>
      <hr style="margin-top: 5px; margin-bottom: 0px;" />
      <div class="clearfix">
        <span class="green-text lastline" style="float: left">
          <i class="el-icon-arrow-up"></i> {{ contestInfo.upvote }}
        </span>
        <span class="red-text lastline" style="float: left">
          <i class="el-icon-arrow-down"></i> {{ contestInfo.downvote }}
        </span>
        <el-button type="text" class="lastline" style="float: right;" @click="detailOnClick">查看详情</el-button>
      </div>
    </div>
  </el-card>
</template>

<script>
import { isoToHumanReadable } from '@/lib/util.js'

export default {
  name: 'ContestCard',
  methods: {
    detailOnClick: function() {
      this.$emit('detail-on-click', this.contestInfo.id)
    }
  },
  props: ['contestInfo'],
  computed: {
    enrollEndHumanReadable: function() {
      return isoToHumanReadable(this.contestInfo.enrollEnd)
    }
  }
}
</script>

<style>
.lastline {
  margin: 5px !important;
  padding: 0px !important;
  font-size: 13px !important;
}

.green-text {
  color: green;
}

.red-text {
  color: darkred;
}

.left-align {
  text-align: left;
  padding-left: 5px;
}

.deadline {
  font-size: 13px;
  color: #999;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: '';
}

.clearfix:after {
  clear: both;
}
</style>
