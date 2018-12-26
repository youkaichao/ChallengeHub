<template>
  <div>
    <el-tabs v-model="currentTabIndex">
      <el-tab-pane v-for="(stage,index) in this.contest.procedure" :key="index" :label="stage.name"></el-tab-pane>
    </el-tabs>
    <el-table :data="submissions">
      <el-table-column label="队伍名称" prop="teamName"></el-table-column>
      <el-table-column label="作品名称" prop="name"></el-table-column>
      <el-table-column label="下载地址">
        <template slot-scope="scope">
          <el-button type="text" @click="downloadWithUrl(scope.row.downloadUrl)">下载</el-button>
        </template>
      </el-table-column>
      <el-table-column label="平均分(点击查看详情)" prop="score" sortable>
        <template slot-scope="scope">
          <el-popover placement="left" trigger="click">
            <el-table :data="scope.row.judges">
              <el-table-column prop="username" label="评委"></el-table-column>
              <el-table-column label="评分">
                <template
                  slot-scope="in_scope"
                >{{in_scope.row.hasReviewed?in_scope.row.score:'未评分'}}</template>
              </el-table-column>
            </el-table>
            <el-button slot="reference">{{scope.row.score}}</el-button>
          </el-popover>
        </template>
      </el-table-column>
      <el-table-column label="附加分" prop="deltaScore" sortable>
        <template slot-scope="scope">
          <el-input-number v-model="scope.row.deltaScore" :controls="false" style="width:80px"></el-input-number>
        </template>
      </el-table-column>
      <el-table-column label="附加分备注">
        <template slot-scope="scope">
          <el-input v-model="scope.row.deltaMsg"></el-input>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            type="text"
            @click="modifyDeltaScore(scope.row.id,scope.row.deltaScore,scope.row.deltaMsg)"
          >修改附加分</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { downloadFile } from '@/lib/util'
export default {
  name: 'ManageSubmission',
  props: ['contest', 'contestId'],
  data() {
    return {
      currentTabIndex: '0',
      submissions: []
    }
  },
  computed: {
    tabIndex() {
      return parseInt(this.currentTabIndex)
    }
  },
  methods: {
    modifyDeltaScore(id, deltaScore, deltaMsg) {
      this.$http
        .post(`/api/contests/${this.contestId}/delta_score/${id}`, {
          deltaScore,
          deltaMsg
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.$message({ type: 'success', message: '修改成功' })
          this.getSubmission()
        })
        .catch(err => {
          this.$message({ type: 'error', message: err.toString() })
        })
    },
    downloadWithUrl(url) {
      downloadFile(document, url)
    },
    getSubmission() {
      if (this.contest.id === -1) {
        // null reference
        return
      }
      if (0 <= this.tabIndex && this.tabIndex < this.contest.procedure.length) {
        this.$http
          .get(`/api/contests/${this.contestId}/submission_all`, {
            params: {
              stage: this.contest.procedure[this.tabIndex].stage + 1
            }
          })
          .then(resp => {
            if (resp.body.code !== 0) {
              throw new Error(resp.body.code + ' ' + resp.body.error)
            }
            this.submissions = resp.body.data
          })
          .catch(err => {
            this.$alert(err.toString())
          })
      }
    }
  },
  created() {
    this.getSubmission()
  },
  watch: {
    contest() {
      this.getSubmission()
    },
    currentTabIndex() {
      this.getSubmission()
    }
  }
}
</script>

<style>
</style>
