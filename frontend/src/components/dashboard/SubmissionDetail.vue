<template>
  <div style="text-align: left; font-size: 20px;">
    <!-- 作品基础信息 -->
    <div>
      <span class="tag">作品名称</span>
      <span>{{detail.submissionName}}</span>
    </div>
    <div>
      <span class="tag">作品分数</span>
      <span>{{detail.score}}</span>
    </div>
    <div>
      <span class="tag">评审人数</span>
      <span>{{detail.reviews.length}}</span>
    </div>
    <div style="text-align: center;">
      <el-button type="primary" @click="handleDownload()">下载作品</el-button>
    </div>

    <h2 style="text-align: center;">评审详情</h2>
    <el-card v-for="(review, index) of detail.reviews" :key="index" style="margin-top: 10px;">
      <div>
        <span class="tag">评审分数</span>
        <span>{{review.rating}}</span>
      </div>
      <div style="margin-top: 10px; font-size: 14px;">
        <span v-if="review.msg === ''" style="color: gray">评委没有填写评语</span>
        <span v-else>
          <div>{{review.msg}}</div>
        </span>
      </div>
    </el-card>
  </div>
</template>

<script>
import { downloadFile } from '@/lib/util.js'

export default {
  props: ['detail'],
  methods: {
    handleDownload() {
      downloadFile(document, this.detail.url)
    }
  }
}
</script>

<style scoped>
.tag {
  color: #409eff;
  margin-right: 10px;
}
</style>
