<template>
  <el-card
    :body-style="{ padding: '0px' }"
    class="burge"
  >
    <el-row style="margin: 0px;">
      <el-col :span="4">
        <img
          :src="contestInfo.imgUrl"
          class="img-in-burge"
          :onerror="defaultImg"
        />
      </el-col>
      <el-col
        :span="16"
        style="text-align: left; padding-left: 20px; padding-top: 15px;"
      >
        <div class="contest-name-burge"> {{contestInfo.name}} </div>
        <div
          class="small-gray-burge"
          style="margin-top: 15px;"
        > <b>比赛学科</b> {{contestInfo.subject}} </div>
        <div class="small-gray-burge"> <b>主办单位</b> {{contestInfo.publisher}} </div>
        <div class="small-gray-burge"> <b>报名截止</b> {{enrollEndHumanReadable}} </div>
      </el-col>
      <el-col :span="4">
        <div style="margin-top: 35px; font-size: 20px;">
          <span class="green-text-burge">
            <i class="el-icon-arrow-up"></i> {{ contestInfo.upvote }}
          </span>
          <span class="red-text-burge">
            <i class="el-icon-arrow-down"></i> {{ contestInfo.downvote }}
          </span>
        </div>
        <div style="margin-top: 30px;">
          <el-button
            type="primary"
            @click="detailOnClick"
          >查看详情</el-button>
        </div>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
import { isoToHumanReadable } from '@/lib/util.js'

export default {
  name: 'ContestCard',
  data() {
    return {
      defaultImg: 'this.src="' + require('@/assets/placeholder.png') + '"'
    }
  },
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

<style scoped>
.green-text-burge {
  color: green;
}

.red-text-burge {
  color: darkred;
}

.contest-name-burge {
  font-size: 28px;
  font-weight: bold;
}

.small-gray-burge {
  color: gray;
}

.burge {
  height: 150px;
}

.img-in-burge {
  max-width: 193px;
  max-height: 150px;
  width: auto;
  height: auto;
}
</style>
