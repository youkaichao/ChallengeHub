<template>
  <div>
    <el-card
      :body-style="{ padding: '0px' }"
      class="single-card"
    >
      <el-row style="margin: 0px;">
        <el-col :span="4">
          <img
            :src="contest.imgUrl"
            class="enrolled-contest-card"
            :onerror="defaultImg"
          >
        </el-col>
        <el-col
          :span="12"
          style="text-align: left; padding-left: 20px;"
        >
          <div class="contest-name">{{ contest.name }}</div>
          <div class="contest-info">{{ contest.publisher }}</div>
          <div class="contest-info">比赛已结束于 {{ endingDeadline }}</div>
          <el-button
            type="text"
            @click="$router.push(`/contest/detail/${contest.id}`)"
          >比赛详情</el-button>
          <el-button
            type="text"
            @click="$router.push(`/contest/notice/${contest.id}`)"
          >比赛公告</el-button>
        </el-col>
        <el-col
          :span="8"
          style="text-align: right; padding-right: 20px;"
        >
          <div class="group-name">{{ group.name }}{{ group.identity }}</div>
          <div class="contest-result">你的成绩：
            <b>{{ group.rank }}</b>
          </div>
          <div style="margin-top: 20px;">
            <el-button
              type="text"
              @click="gotoMyTeam"
              style="display:inline-block"
            >查看我的队伍</el-button>
            <el-button
              type="primary"
              plain
              @click="downloadDialogVisible = true"
            >下载作品</el-button>
            <el-button
              type="primary"
              @click="resultDetailVisible = true"
            >查看结果详情</el-button>
          </div>
        </el-col>
      </el-row>
    </el-card>

    <el-dialog
      title="下载作品"
      :visible.sync="downloadDialogVisible"
      :width="'30%'"
    >
      <div
        v-for="(name, index) of downloadableStageNames"
        :key="index"
        style="margin-top: 10px;"
      >
        <el-button
          type="primary"
          plain
          @click="handleDownload(index)"
        >下载
          <span style="font-weight: bold;">{{name}}</span>阶段提交
        </el-button>
      </div>
    </el-dialog>

    <el-dialog
      title="比赛结果详情"
      :visible.sync="resultDetailVisible"
    >
      <p v-if="group.stage === -1">祝贺！你通过了比赛的所有阶段，最终获得
        <span class="blue-bold">{{group.rank}}</span> 的成绩！
      </p>
      <p v-else>你坚持到了比赛的
        <span class="blue-bold">{{contest.procedure[(group.stage / 2) - 1].name}}</span> 阶段，下次加油！
      </p>
      <div
        v-for="(name, index) of downloadableStageNames"
        :key="index"
      >
        <el-button
          type="primary"
          style="margin-top: 10px;"
          @click="handelCheckDetail(index)"
        >查看
          <b>{{name}}</b> 阶段评审详情
        </el-button>
      </div>
    </el-dialog>

    <el-dialog
      title="过往作品详情"
      :visible.sync="reviewDetailVisible"
    >
      <submission-detail :detail="selectedDetail" />
    </el-dialog>
  </div>
</template>

<script>
import { isoToHumanReadable, downloadFile } from '@/lib/util.js'
import SubmissionDetail from './SubmissionDetail.vue'

export default {
  name: 'EnrolledContestFinished',
  computed: {
    endingDeadline: function() {
      let procedure = this.contest.procedure
      let deadline = procedure[procedure.length - 1].endTime
      return isoToHumanReadable(deadline)
    },
    downloadableStageNames() {
      let ret = []
      let stage = this.group.stage
      if (stage === -1) {
        stage = this.contest.procedure.length * 2
      }

      for (let i = 0; i < stage / 2; i++) {
        ret.push(this.contest.procedure[i].name)
      }

      return ret
    }
  },
  props: ['contest', 'group'],
  methods: {
    gotoMyTeam() {
      this.$router.push({
        name: 'mygroup',
        params: {
          id: this.contest.id
        }
      })
    },
    async handleDownload(index) {
      let stage = (index + 1) * 2
      let response = await this.$http.get(`/api/contests/${this.contest.id}/submissions`, { params: { stage } })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }
      downloadFile(document, response.body.data.url)
    },
    async handelCheckDetail(index) {
      let stage = (index + 1) * 2
      let response = await this.$http.get(`/api/contests/${this.contest.id}/submissions&stage=${stage}`)
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }
      this.selectedDetail = response.body.data
      this.reviewDetailVisible = true
    }
  },
  data() {
    return {
      downloadDialogVisible: false,
      resultDetailVisible: false,
      reviewDetailVisible: false,
      selectedDetail: null,
      defaultImg: 'this.src="' + require('@/assets/placeholder.png') + '"'
    }
  },
  components: {
    'submission-detail': SubmissionDetail
  }
}
</script>

<style scoped>
.single-card {
  height: 150px;
  margin-left: 10px;
  margin-right: 10px;
}

.enrolled-contest-card {
  max-width: 200px;
  max-height: 152px;
  width: auto;
  height: auto;
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

.contest-result {
  margin-top: 5px;
  color: gray;
}

.blue-bold {
  color: #409eff;
  font-weight: bold;
}
</style>
