<template>
  <div>
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
          <el-select v-model="currentSelected" placeholder="请选择一个阶段">
            <el-option v-for="(stage, index) of reviewableStages" :key="index" :label="stage.name" :value="stage.index">
            </el-option>
          </el-select>
          <el-button type="primary" plain style="margin-left: 20px;" @click="switchStage(currentSelected)">查看其它阶段评审</el-button>
        </el-row>
        <div class="section-header" style="color: ">
          阶段 <span style="color: #409eff;">{{currentStage}}</span> 评审进度
        </div>
        <el-progress style="margin-top: 15px; margin-bottom: 50px;" :percentage="parseFloat((task.done * 100 / task.count).toFixed(1))" :text-inside="true" :stroke-width="18" />

        <div class="section-header">
          选手作品
        </div>
        <el-row type="flex" style="justify-content: space-between;">
          <el-button :disabled="readonly" type="primary" @click="commitReviews()">保存评审</el-button>
          <span>
            <el-button :disabled="readonly" type="primary" @click="downloadAll()" plain>下载所有作品</el-button>
            <el-button :disabled="readonly" type="primary" @click="downloadUnreviewed()">下载未评审作品</el-button>
          </span>
        </el-row>
        <judge-submission v-for="(item, index) in wrappedSubmissions" :key="item.guid" :title="item.submission.title" :number="index + 1" :reviewed="item.submission.reviewed" :rating="item.submission.rating" style="margin-bottom: 10px" :readonly="readonly" v-on:rate="handleRate" v-on:remark="handleRemark" v-on:download="downloadOne" v-on:check="handleCheck" />
        <el-row type="flex" style="justify-content: space-between; margin-top: 20px;">
          <el-button :disabled="readonly" type="primary" @click="commitReviews">保存评审</el-button>
          <span>
            <el-button :disabled="readonly" type="primary" @click="downloadAll()" plain>下载所有作品</el-button>
            <el-button :disabled="readonly" type="primary" @click="downloadUnreviewed()">下载未评审作品</el-button>
          </span>
        </el-row>
      </el-col>
    </el-row>

    <el-dialog title="撰写评语" :visible.sync="remarkDialogVisible" :width="'30%'">
      <el-input type="textarea" v-model="currentRemark">
      </el-input>
      <el-button style="margin-top: 20px;" type="primary" @click="handleRemarkConfirm">确定</el-button>
    </el-dialog>
  </div>
</template>

<script>
import JudgeSubmission from './JudgeSubmission'
import { downloadFile, guid } from '@/lib/util.js'

export default {
  name: 'JudgeWorkspace',
  data() {
    return {
      currentSelected: '',
      contest: {},
      task: {},
      submissions: [],
      readonly: false,
      currentStage: '',
      dirty: new Set([]),
      currentRemark: '',
      currentRemarkNumber: null,
      remarkDialogVisible: false
    }
  },
  components: {
    'judge-submission': JudgeSubmission
  },
  methods: {
    async commitReviews() {
      try {
        let ret = []
        for (let dirtyNumber of this.dirty) {
          let instance = this.submissions[dirtyNumber - 1]
          ret.push({
            id: instance.id,
            reviewed: true,
            rating: instance.rating
          })
        }
        let data = { reviews: ret }

        let response = await this.$http.post(`/api/judges/${this.contest.id}`, data)
        if (response.body.code !== 0) {
          this.$message({ type: 'error', message: response.body.error })
        } else {
          this.$message({ type: 'sucess', message: '提交成功' })
          await this.initializeData()
        }
      } catch (error) {
        this.$message({ type: 'error', message: '提交失败，发生意外错误' })
      }
    },
    downloadAll() {
      for (let i = 1; i < this.submissions.length; i++) {
        let extension = this.submissions[i - 1].extension
        let filename = extension === '' ? `${i}.${extension}` : `${i}`
        downloadFile(document, this.submissions[i - 1].url, filename)
      }
    },
    async downloadUnreviewed() {
      for (let i = 1; i < this.submissions.length; i++) {
        if (!this.submissions[i - 1].reviewed) {
          let extension = this.submissions[i - 1].extension
          let filename = extension === '' ? `${i}.${extension}` : `${i}`
          downloadFile(document, this.submissions[i - 1].url, filename)
        }
      }
    },
    downloadOne(index) {
      let extension = this.submissions[index - 1].extension
      let filename = extension === '' ? `${index}.${extension}` : `${index}`
      downloadFile(document, this.submissions[index - 1].url, filename)
    },
    handleRate({ number, rating }) {
      this.submissions[number - 1].rating = rating
    },
    handleRemark(number) {
      this.currentRemark = ''
      this.currentRemarkNumber = number
      this.remarkDialogVisible = true
    },
    handleRemarkConfirm() {
      this.$message({ type: 'success', message: '正在假装评语发送成功' })
      this.currentRemark = ''
      this.currentRemarkNumber = null
      this.remarkDialogVisible = false
    },
    handleCheck(number) {
      this.dirty.add(number)
    },
    async switchStage(index) {
      if (index === null || index === '') {
        this.$message({ type: 'error', message: '无效的阶段名' })
      } else if (parseInt(index) > this.contest.stage) {
        this.$message({ type: 'error', message: '阶段尚未开始' })
      } else {
        let result = await this.initializeData(index)
        if (result) {
          this.$message({ type: 'success', message: '已切换阶段' })
        }
      }
    },
    async initializeData(stage) {
      let response = null
      if (stage === null) {
        response = await this.$http.get(`/api/judges/${this.$route.params.id}`)
      } else {
        response = await this.$http.get(`/api/judges/${this.$route.params.id}&stage=${stage}`)
      }

      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return false
      }

      let data = response.body.data
      this.contest = data.contest
      this.task = data.task
      this.submissions = data.submissions

      if (stage !== null && stage !== response.body.data.contest.stage) {
        this.readonly = true
      } else {
        this.readonly = false
      }

      if (stage === null) {
        this.currentStage = this.contest.procedure[this.contest.stage / 2 - 1].name
      } else {
        this.currentStage = this.contest.procedure[stage / 2 - 1].name
      }

      this.dirty = new Set([])
      this.currentRemark = ''
      this.currentRemarkNumber = ''
      this.remarkDialogVisible = false

      return true
    }
  },
  async created() {
    await this.initializeData(null)
  },
  computed: {
    reviewableStages() {
      if (this.contest === null) return []
      let procedure = this.contest.procedure
      for (let i = 0; i < procedure.length; i++) {
        procedure[i]['index'] = (i + 1) * 2
      }
      return procedure
    },
    wrappedSubmissions() {
      let ret = []
      for (let submission of this.submissions) {
        ret.push({ guid: guid(), submission: submission })
      }
      return ret
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
  color: gray;
  font-weight: bold;
  font-size: 24px;
}
</style>
