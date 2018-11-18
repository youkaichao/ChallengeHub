<template>
  <div>
    <el-tabs v-model="currentTabIndex">
      <el-tab-pane v-for="(stage,index) in this.contest.procedure" :key="index" :label="stage.name">
      </el-tab-pane>
    </el-tabs>
    <el-table :data="submissions">
      <el-table-column label="队伍名称" prop="teamName"></el-table-column>
      <el-table-column label="作品名称" prop="name"></el-table-column>
      <el-table-column label="提交时间" prop="submissionTime"></el-table-column>
      <el-table-column label="平均分(点击查看详情)">
        <template slot-scope="scope" prop="average" sortable>
          <el-popover placement="left" trigger="click">
            <el-table :data="scope.row.judges">
              <el-table-column prop="name" label="评委"></el-table-column>
              <el-table-column label="评分">
                <template slot-scope="in_scope">
                  {{in_scope.row.judged?in_scope.row.score:'未评分'}}
                </template>
              </el-table-column>
            </el-table>
            <el-button slot="reference">{{scope.row.average}}</el-button>
          </el-popover>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'ManageSubmission',
  props: ['contest', 'contestId'],
  data() {
    return {
      currentTabIndex: '1',
      submissions: []
    }
  },
  computed: {
    tabIndex() {
      return parseInt(this.currentTabIndex)
    }
  },
  methods: {
    getSubmission() {
      if (!this.contest) {
        // null reference
        return
      }
      this.stages = []
      for (let i = 0; i < this.contest.procedure.length; i++) {
        let step = this.contest.procedure[i]
        this.stages.push({
          name: step.name,
          submission: []
        })
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
            this.stages.splice(i, 1, {
              name: step.name,
              submission: resp.body.data
            })
            this.submissions = resp.body.data
          })
          .catch(err => {
            this.$alert(err)
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
