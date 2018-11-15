<template>
  <el-row :gutter="20">
    <el-col :span="12">
      <el-row style="height: 150px;" :gutter="0">
        <el-col :span="8">
          <img :src="contest.imgUrl" style="width: 100%" />
        </el-col>
        <el-col :span="16" style="text-align: left;">
          <div class="flex-box" style="height: 140px; margin-left: 20px;">
            <h1 class="no-margin">{{contest.name}}</h1>
            <span style="color: gray;">{{contest.publisher}}</span>
          </div>
        </el-col>
      </el-row>
      <mavon-editor v-model="contest.standard" :editable="false" :defaultOpen="'preview'" :subfield="false" :toolbarsFlag="false" :boxShadow="false" />
    </el-col>
    <el-col :span="12">
      <el-row style="text-align: right; margin-bottom: 60px;">
        <el-select v-model="currentState" placeholder="请选择一个阶段">
          <el-option v-for="(stage, index) of stages" :key="index" :label="stage.name" :value="stage.index">
          </el-option>
        </el-select>
        <el-button type="primary" plain style="margin-left: 20px;">查看其它阶段评审结果</el-button>
      </el-row>
      <div class="section-header">
        当前评审进度
      </div>
      <el-progress style="margin-top: 15px; margin-bottom: 50px;" :percentage="(task.done * 100 / task.count).toFixed(1)" :text-inside="true" :stroke-width="18" />

      <div class="section-header">
        选手作品
      </div>
      <el-row type="flex" style="justify-content: space-between;">
        <el-button type="primary">保存评审</el-button>
        <el-button type="primary">下载所有作品</el-button>
      </el-row>
      <judge-submission v-for="(item, index) in submissions" :key="index" :title="item.title" :number="index + 1" :reviewed="item.reviewed" :rating="item.rating" style="margin-bottom: 10px" />
      <el-row type="flex" style="justify-content: space-between; margin-top: 20px;">
        <el-button type="primary">保存评审</el-button>
        <el-button type="primary">下载所有作品</el-button>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
import JudgeSubmission from './JudgeSubmission'
export default {
  name: 'JudgeWorkspace',
  data() {
    return {
      currentState: '',
      contest: null,
      task: null,
      submissions: []
    }
  },
  components: {
    'judge-submission': JudgeSubmission
  },
  async created() {
    let response = await this.$http.get(`/api/judge/contests/${this.$route.params.id}/submissions`)
    if (response.body.code !== 0) {
      alert(response.body.error)
      return
    }
    let data = response.body.data
    this.contest = data.contest
    this.task = data.task
    this.submissions = data.submissions
  },
  computed: {
    stages() {
      if (this.contest === null) return [];
      let procedure = JSON.parse(this.contest.procedure);
      for(let i = 0;i<procedure.length; i++) {
        procedure[i]['index'] = (i + 1) * 2;
      }
      return procedure;
    }
  }
}
</script>

<style scoped>
.flex-box {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.no-margin {
  margin: 0;
}

.section-header {
  color: #409eff;
  font-weight: bold;
  font-size: 24px;
}
</style>
