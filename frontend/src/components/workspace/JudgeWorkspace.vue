<template>
  <div>
    <!-- 顶部信息 -->
    <el-row :gutter="20">
      <el-col :span="12">
        <!-- 比赛信息 -->
        <el-row style="height: 150px;" :gutter="0">
          <el-col :span="8">
            <img :src="contest.imgUrl" class="fix-img" :onerror="defaultImg">
          </el-col>
          <el-col :span="16" style="text-align: left;">
            <div class="flex-box" style="height: 140px; margin-left: 20px;">
              <h1 class="no-margin">{{contest.name}}</h1>
              <span style="color: gray;">{{contest.publisher}}</span>
            </div>
          </el-col>
        </el-row>
      </el-col>
      <el-col :span="12">
        <!-- 切换阶段与下载 -->
        <el-row style="text-align: right; margin-bottom: 50px;">
          <el-select v-model="currentSelected" placeholder="请选择一个阶段">
            <el-option
              v-for="(stage, index) of reviewableStages"
              :key="index"
              :label="stage.name"
              :value="stage.index"
            ></el-option>
          </el-select>
          <el-button
            type="primary"
            plain
            style="margin-left: 20px;"
            @click="switchStage(currentSelected)"
          >查看其它阶段评审</el-button>
        </el-row>
        <el-row type="flex" style="flex-direction: row-reverse;">
          <el-button
            :disabled="readonly"
            type="success"
            @click="downloadUnreviewed()"
            style="margin-left: 10px;"
          >下载未评审作品</el-button>
          <el-button :disabled="readonly" type="success" @click="downloadAll()" plain>下载所有作品</el-button>
        </el-row>
      </el-col>
    </el-row>
    <!-- 顶部信息结束 -->
    <!-- 进度条信息 -->
    <div class="section-header" style="color: ">
      <span v-if="typeof(currentStage) === 'string'">阶段<span style="color: #409eff;">{{currentStage}}</span> 评审进度</span>
      <span v-else-if="currentStage.special === 'beforeStart'">比赛尚未开始</span>
      <span v-else-if="currentStage.special === 'afterEnd'">比赛已经结束</span>
      <span v-else>未知的比赛阶段</span>
    </div>
    <el-progress
      style="margin-top: 15px; margin-bottom: 50px; width: 800px; margin-left: auto; margin-right: auto;"
      :percentage="(task.count === 0 ? 1.0 : parseFloat((task.done * 100 / task.count).toFixed(1))) || 1.0"
      :text-inside="true"
      :stroke-width="18"
    />
    <!-- 进度条信息结束 -->
    <!-- 选手提交 -->
    <div class="section-header" style="color: ">选手提交</div>
    <el-table
      :data="submissions"
      stripe
      style="width: 100%"
      :default-sort="{prop: 'tag', order: 'ascending'}"
    >
      <el-table-column prop="tag" label="序号" width="100"></el-table-column>
      <!-- // ! 该接口目前尚未提供 -->
      <el-table-column prop="groupName" label="小组名称" width="200"></el-table-column>
      <el-table-column prop="submissionName" label="作品名称" min-width="400"></el-table-column>
      <el-table-column label="评分" width="150">
        <template slot-scope="scope">
          <span>{{scope.row.reviewed ? scope.row.rating : "未评审"}}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="100">
        <template slot-scope="scope">
          <el-button v-if="readonly" plain type="primary" @click="handleDetail(scope.row)">查看</el-button>
          <el-button
            v-if="!readonly"
            :plain="scope.row.reviewed"
            type="primary"
            @click="handleDetail(scope.row)"
          >{{scope.row.reviewed?"修改":"评审"}}</el-button>
        </template>
      </el-table-column>
    </el-table>
    <!-- 选手提交结束 -->
    <!-- 评审弹出窗口 -->
    <el-dialog title="评审作品" :visible.sync="remarkDialogVisible" :width="'60%'">
      <h2 style="margin-top: 0px; margin-bottom: 0px;">
        作品
        <span style="color: #409eff; margin-left; 20px;">{{currentSubmission.submissionName}}</span>
      </h2>
      <h2 style="margin-top: 0px; margin-bottom: 0px;">
        小组
        <span style="color: #409eff; margin-left; 20px;">{{currentSubmission.groupName}}</span>
      </h2>

      <el-button
        @click="downloadSubmission(currentSubmission)"
        type="primary"
        style="margin-top: 20px;"
      >下载作品</el-button>

      <div style="font-size: 20px; margin-top: 20px;">
        <span>当前状态</span>
        <span
          style="margin-left: 20px; color: #409eff;"
        >{{currentSubmission.reviewed ? "已评审":"未评审"}}</span>
      </div>

      <div style="margin-top: 20px;">
        <span style="font-size: 20px;">作品评分</span>
        <el-input-number
          style="margin-left: 20px;"
          v-model="currentRating"
          controls-position="right"
          :min="0"
          :max="100"
          :disabled="readonly"
        ></el-input-number>
        <el-button
          style="margin-left: 20px;"
          @click="standardDialogVisible=true"
          type="primary"
          plain
        >显示评分细则</el-button>
      </div>

      <h2>评语（可选）</h2>
      <el-input
        type="textarea"
        :rows="10"
        placeholder="请输入评语"
        v-model="currentRemark"
        :disabled="readonly"
      >{{currentSubmission.msg}}</el-input>

      <el-button
        :disabled="readonly"
        type="primary"
        style="margin-top: 20px;"
        @click="confirmRemark"
      >提交评审</el-button>
    </el-dialog>

    <!-- 评分细则窗口 -->
    <el-dialog title="评分细则" :visible.sync="standardDialogVisible" :width="'60%'">
      <mavon-editor
        v-model="contest.standard"
        :editable="false"
        :defaultOpen="'preview'"
        :subfield="false"
        :toolbarsFlag="false"
        :boxShadow="false"
      />
    </el-dialog>
  </div>
</template>

<script>
import { downloadFile } from '@/lib/util.js'

export default {
  name: 'JudgeWorkspace',
  data() {
    return {
      defaultImg: 'this.src="' + require('@/assets/placeholder.png') + '"',
      currentSelected: '', // 当前选择的阶段
      contest: {}, // 当前比赛的信息
      task: {}, // 当前任务信息
      submissions: [],
      readonly: false,
      currentStage: '',
      currentRemark: '',
      remarkDialogVisible: false,
      standardDialogVisible: false,
      currentSubmission: {},
      currentRating: 0
    }
  },
  async created() {
    await this.initializeData(null)
  },
  methods: {
    async initializeData(stage) {
      let response = null

      try {
        if (stage === null || stage === undefined) {
          response = await this.$http.get(`/api/judges/${this.$route.params.id}`)
        } else {
          response = await this.$http.get(`/api/judges/${this.$route.params.id}`, {
            params: {
              stage
            }
          })
        }
      } catch (error) {
        this.$message({ type: 'error', message: '数据刷新失败' })
        return false
      }

      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return false
      }

      if (response.body.data.contest.stage === -1 && (stage === null || stage === undefined)) {
        let lastStage = response.body.data.contest.procedure.length * 2
        await this.initializeData(lastStage)
        return
      }

      let data = response.body.data
      this.contest = data.contest
      this.task = data.task
      this.submissions = data.submissions

      // append tag to each submission
      for (let i = 0; i < this.submissions.length; i++) {
        this.submissions[i].tag = i + 1
      }

      if (stage !== null && stage !== undefined && stage !== response.body.data.contest.stage) {
        this.readonly = true
      } else {
        this.readonly = false
      }

      if (stage === null || stage === undefined) {
        if(this.contest.stage === 0) {
          this.currentStage = {special: 'beforeStart'}
        } else if(this.contest.stage === -1) {
          this.currentStage = {special: 'afterEnd'}
        } else {
          this.currentStage = this.contest.procedure[this.contest.stage / 2 - 1].name
        }
      } else {
        this.currentStage = this.contest.procedure[stage / 2 - 1].name
      }

      this.currentRemark = ''

      return true
    },
    async switchStage(index) {
      if (index === null || index === '') {
        this.$message({ type: 'error', message: '无效的阶段名' })
      } else if (this.contest.stage >= 0 && parseInt(index) > this.contest.stage) {
        this.$message({ type: 'error', message: '阶段尚未开始' })
      } else {
        let result = await this.initializeData(index)
        if (result) {
          this.$message({ type: 'success', message: '已切换阶段' })
        }
      }
    },
    handleDetail(submission) {
      this.remarkDialogVisible = true
      this.currentSubmission = submission
      this.currentRemark = submission.msg
      this.currentRating = submission.rating
    },
    async confirmRemark() {
      let payload = {
        reviews: [
          {
            id: this.currentSubmission.id,
            reviewed: true,
            rating: this.currentRating,
            msg: this.currentRemark
          }
        ]
      }

      let response = await this.$http.post(`/api/judges/${this.contest.id}`, payload)
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      } else {
        this.$message({ type: 'success', message: '提交成功' })
      }

      await this.initializeData()
    },
    downloadSubmission(submission) {
      let fileName
      if (submission.extension === '') {
        fileName = `${submission.tag}`
      } else {
        fileName = `${submission.tag}.${submission.extension}`
      }
      downloadFile(document, submission.url, fileName)
    },
    downloadAll() {
      for (let submission of this.submissions) {
        let fileName
        if (submission.extension === '') {
          fileName = `${submission.tag}`
        } else {
          fileName = `${submission.tag}.${submission.extension}`
        }

        downloadFile(document, submission.url, fileName)
      }
    },
    downloadUnreviewed() {
      for (let submission of this.submissions) {
        if (submission.reviewed) continue
        let fileName
        if (submission.extension === '') {
          fileName = `${submission.tag}`
        } else {
          fileName = `${submission.tag}.${submission.extension}`
        }

        downloadFile(document, submission.url, fileName)
      }
    }
  },
  computed: {
    reviewableStages() {
      if (!this.contest || !this.contest.procedure) return []
      let procedure = this.contest.procedure
      for (let i = 0; i < procedure.length; i++) {
        procedure[i]['index'] = (i + 1) * 2
      }
      return procedure
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

.fix-img {
  max-width: 190px;
  max-height: 142px;
  width: auto;
  height: auto;
}
</style>