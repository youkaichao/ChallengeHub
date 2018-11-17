<template>
  <div>
    <el-card :body-style="{ padding: '0px' }" class="single-card">
      <el-row style="margin: 0px;">
        <el-col :span="4">
          <img :src="contest.imgUrl" class="enrolled-contest-card" />
        </el-col>
        <el-col :span="12" style="text-align: left; padding-left: 20px;">
          <div class="contest-name"> {{ contest.name }} </div>
          <div class="contest-info"> {{ contest.publisher }} </div>
          <div v-if="contest.stage === 0" class="contest-info">已报名，比赛尚未开始</div>
          <div v-else-if="contest.stage !== 0 && contest.stage % 2 === 1" class="contest-info">提交中，当前阶段 <b>{{ currentStage }}</b> 结束于 <b>{{ currentDeadline }}</b></div>
          <div v-else-if="contest.stage !== 0 && contest.stage % 2 === 0 && !isLastStage" class="contest-info">审核中，下一阶段 <b>{{ currentStage }}</b> 开始于 <b>{{ currentDeadline }}</b></div>
          <div v-else-if="isLastStage" class="contest-info">审核中，请等待比赛结果</div>
          <el-button type="text" @click="$router.push(`/contest/detail/${contest.id}`)">查看比赛详情</el-button>
        </el-col>

        <!--选手查看的信息-->
        <el-col :span="8" style="text-align: right; padding-right: 20px;">
          <div class="group-name">
            <span> {{ group.name }}{{ group.identity }} </span>
          </div>
          <div class="commit-status">
            <span v-if="isCommitStage && group.hasCommit">作品已提交</span>
            <span v-if="isCommitStage && (!group.hasCommit)"><span style="color: #E6A23C; font-weight: bold;">作品未提交</span></span>
            <span v-if="!isCommitStage">当前无法提交作品</span>
          </div>
          <div style="margin-top: 5px;">
            <el-button v-if="downloadableStageNames.length !== 0" type="text" style="padding: 0;" @click="downloadDialogVisible = true">下载过往作品</el-button>
            <el-button v-else type="text" style="padding: 0;" disabled>无过往作品</el-button>
          </div>
          <el-upload v-show="isCommitStage && (!group.hasCommit)" :limit="1" :http-request="handleUpload" action="" style="display: inline-block">
            <el-button type="primary" class="commit-button">提交作品</el-button>
          </el-upload>
          <el-upload v-show="isCommitStage && group.hasCommit" :limit="1" :http-request="handleUpload" action="" style="display: inline-block">
            <el-button type="primary" class="commit-button" plain>修改作品</el-button>
          </el-upload>
          <el-button v-show="isCommitStage && group.hasCommit" type="primary" @click="handleDownload(null)" class="commit-button" plain>下载提交作品</el-button>
        </el-col>
      </el-row>
    </el-card>

    <el-dialog title="下载作品" :visible.sync="downloadDialogVisible" :width="'30%'">
      <div v-for="(name, index) of downloadableStageNames" :key="index" style="margin-top: 10px;">
        <el-button type="primary" plain @click="handleDownload(index)">下载<span style="font-weight: bold;"> {{name}} </span>阶段提交</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { isoToHumanReadable, downloadFile } from '@/lib/util.js'

export default {
  name: 'EnrolledContestUnfinished',
  data() {
    return {
      downloadDialogVisible: false
    }
  },
  methods: {
    async handleUpload(param) {
      try {
        let result = await this.$prompt('请输入作品名', '请输入作品名', {
          confirmButtonText: '确定',
          cancelButtonText: '取消'
        })

        let name = result.value
        let file = param.file

        var form = new FormData()
        form.append('file', file)
        form.append('groupId', this.group.id)
        form.append('submissionName', name)

        let response = await this.$http.post(`/api/contests/${this.contest.id}/submissions`, form)
        if (response.body.code !== 0) {
          this.$message({ type: 'error', message: '上传失败' })
        } else {
          this.$message({ type: 'info', message: '上传成功' })
          this.group.hasCommit = true
        }
      } catch (error) {
        this.$message({ type: 'error', message: `上传取消或失败` })
        return
      }
    },
    async handleDownload(index) {
      let response = null
      if (index === null) {
        response = await this.$http.get(`/api/contests/${this.contest.id}/submissions`)
      } else {
        let stage = (index + 1) * 2
        response = await this.$http.get(`/api/contests/${this.contest.id}/submissions&stage=${stage}`)
      }
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }
      downloadFile(document, response.body.data.url)
    }
  },
  props: ['contest', 'group'],
  computed: {
    currentStage: function() {
      let stageIndex = this.contest.stage
      let procedure = this.contest.procedure
      if (stageIndex === 0 || stageIndex === 2 * procedure.length) return ''
      if (stageIndex % 2 !== 0) {
        return procedure[(stageIndex - 1) / 2].name
      } else {
        return procedure[stageIndex / 2].name
      }
    },
    currentDeadline: function() {
      let stageIndex = this.contest.stage
      let procedure = this.contest.procedure
      let returnDate = null
      if (stageIndex === 0 || stageIndex === 2 * procedure.length) return ''
      if (stageIndex % 2 !== 0) {
        returnDate = procedure[(stageIndex - 1) / 2].endTime
      } else {
        returnDate = procedure[stageIndex / 2].startTime
      }

      return isoToHumanReadable(returnDate)
    },
    isLastStage() {
      return this.contest.stage === this.contest.procedure.length * 2
    },
    isCommitStage() {
      return this.contest.stage > 0 && this.contest.stage % 2 === 1
    },
    downloadableStageNames() {
      let ret = []
      let stage = this.group.stage

      if (stage === -1) {
        stage = this.contest.procedure.length * 2
      } else if (stage % 2 === 1) {
        stage -= 1
      }

      for (let i = 0; i < stage / 2; i++) {
        ret.push(this.contest.procedure[i].name)
      }

      return ret
    }
  }
}
</script>

<style scoped>
.single-card {
  height: 150px;
}

.enrolled-contest-card {
  width: 100%;
}

.contest-name {
  margin-top: 10px;
  font-weight: bold;
  font-size: 32px;
}

.contest-info {
  margin-top: 5px;
  color: grey;
}

.group-name {
  margin-top: 10px;
  font-weight: bold;
  font-size: 24px;
}

.commit-status {
  color: gray;
}

.commit-button {
  margin-top: 5px;
  margin-left: 20px;
}
</style>
