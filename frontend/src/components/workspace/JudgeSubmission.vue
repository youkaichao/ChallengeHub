<template>
  <el-card class="judge-submission-card" :body-style="{ padding: '0px' }">
    <el-row>
      <el-col :span="12">
        <div class="flex-box align-left" style="height: 100px;">
          <h1 class="no-margin">{{title}}</h1>
          <h1 class="submission-number no-margin"># {{number}}</h1>
          <div v-if="!readonly && isClean" class="no-margin" style="color: #67C23A;">已暂存</div>
          <div v-else-if="reviewed" class="no-margin" style="color: #cccccc;">已评审</div>
          <div v-else class="no-margin" style="color: #E6A23C;">未评审</div>
        </div>
      </el-col>
      <el-col :span="12">
        <div class="flex-box align-right" style="height: 100px;">
          <div>
            <span style="margin-right: 20px; color: gray;">评分</span>
            <el-input-number style="width: 120px;" :disabled="readonly" v-model="currentRating" controls-position="right" @change="$emit('rate', {number: number, rating: currentRating})" :min="0" :max="100"></el-input-number>
            <el-button v-if="!readonly" type="primary" icon="el-icon-check" style="margin-left: 20px;" :plain="isClean ? true : false" @click="handleCheck" />
          </div>
          <div>
            <el-button v-if="!readonly" type="primary" plain @click="$emit('remark', number)">撰写评语</el-button>
            <el-button v-if="!readonly && !reviewed" type="primary" @click="$emit('download', number)">下载作品</el-button>
            <el-button v-if="!readonly && reviewed" type="primary" plain @click="$emit('download', number)">下载作品</el-button>
            <el-button v-if="readonly" type="primary" plain @click="$emit('download', number)">下载作品</el-button>
          </div>
        </div>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
export default {
  name: 'JudgeSubmission',
  props: ['title', 'number', 'reviewed', 'rating', 'readonly'],
  methods: {
    handleCheck() {
      this.isClean = true
      this.$emit('check', this.number)
    }
  },
  data() {
    return {
      currentRating: this.rating,
      isClean: false
    }
  }
}
</script>

<style scoped>
.judge-submission-card {
  height: 120px;
}

.flex-box {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.align-left {
  text-align: left;
}

.align-right {
  text-align: right;
}

.submission-number {
  font-weight: bold;
  color: #409eff;
}

.no-margin {
  margin: 0;
}
</style>
