<template>
  <div>
    <el-row>
      当前阶段: {{ stageName }}
    </el-row>
    <div v-show="!isNull">
      <mavon-editor v-model="criterion" placeholder="在这里输入评分标准" />
      <el-row>
        <el-col :span="4">
          <el-button type="infor" @click="modifyCriterion">
            修改评分标准
          </el-button>
        </el-col>
      </el-row>
    </div>
    <p v-show="tried">有{{groupNotFull}}个作品没有达到{{maxconn}}个选手评，有{{groupZero}}个作品没有人评</p>
    <el-table :data="reviewers">todo
      <el-table-column width="160" label="评委用户名" prop="username"></el-table-column>
      <el-table-column label="邮箱" prop="email"></el-table-column>
      <el-table-column width="60" label="被分配数" prop="assigned"></el-table-column>
      <el-table-column width="60" label="已完成数" prop="completed"></el-table-column>
      <el-table-column label="评审进度">
        <template slot-scope="scope">
          <el-progress :percentage="getPercentage(scope.row.completed,scope.row.assigned)"></el-progress>
        </template>
      </el-table-column>
      <el-table-column label="目标被分配数">
        <template slot-scope="scope">
          <el-input-number controls-position="right" :min="0" v-model="scope.row.targetAssigned"></el-input-number>
        </template>
      </el-table-column>
    </el-table>
    <el-row align="middle">
      <el-col :span="6">每个作品最多评委数</el-col>
      <el-col :span="8">
        <el-input-number v-model="maxconn" :min="0" controls-position="right"></el-input-number>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="5">
        <el-button type="infor" @click="evenlyDistribute">一键平均分配提交</el-button>
      </el-col>
      <el-col :span="4">
        <el-button :disabled="stat.isAssigned||!isJudge" type="primary" @click="calcAssign(false)">{{isJudge?'计算分配方案':'只有在评审阶段能分配任务'}}</el-button>
      </el-col>
      <el-col :span="4">
        <el-button :disabled="stat.isAssigned||!tried||!isJudge" type="warning" @click="calcAssign(true)">应用分配方案</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { getContestStage, getPercentage, isJudgeStage, isNullStage } from '@/lib/util'
export default {
  name: 'ManageReview',
  props: ['contest', 'contestId'],
  data() {
    return {
      maxconn: 1,
      tried: false,
      stat: {
        totalTasks: 0,
        reviewedTasks: 0,
        qualifiedGroups: 0,
        submittedGroups: 0,
        isAssigned: true // 是否之前一键分配过
      },
      criterion: '',
      reviewers: [],
      groupNotFull: 0, // 没有评满的队伍数
      groupZero: 0
    }
  },
  computed: {
    isJudge() {
      return isJudgeStage(this.contest.stage)
    },
    stageName() {
      if (this.contest.id === -1) {
        return '阶段名称'
      }
      return getContestStage(this.contest.procedure, this.contest.stage)
    },
    isNull() {
      return isNullStage(this.contest.stage)
    }
  },
  methods: {
    getPercentage,
    isJudgeStage,
    evenlyDistribute() {
      if (this.reviewers.length === 0) {
        this.$alert('没有评委')
        return
      }
      let total = this.maxconn * this.stat.submittedGroups
      let eachOne = Math.ceil(total / this.reviewers.length)
      for (let reviewer of this.reviewers) {
        reviewer.targetAssigned = eachOne
      }
    },
    calcAssign(serious) {
      if (serious) {
        this.$confirm('应用之后分配方案不可修改，确认要继续吗？')
          .then(() => {
            this.reallyAssign(serious)
          })
          .catch(() => {})
      } else {
        this.reallyAssign(serious)
      }
    },
    reallyAssign(serious) {
      let judges = []
      for (let reviewer of this.reviewers) {
        judges.push({
          username: reviewer.username,
          assign: reviewer.targetAssigned
        })
      }
      this.$http
        .post(`/api/contests/${this.contestId}/auto_assign`, {
          stage: this.contest.stage,
          serious, // 是否需要应用到数据库
          maxconn: this.maxconn, // 每个作品最多几个选手评
          judges
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.groupNotFull = resp.body.data.groupNotFull
          this.groupZero = resp.body.data.groupZero
          if (serious) {
            this.refreshReview()
            this.refreshStat()
          } else {
            let nextJudges = resp.body.data.judges
            for (let i = 0; i < nextJudges.length; i++) {
              for (let j = 0; j < this.reviewers.length; j++) {
                let reviewer = this.reviewers[(i + j) % this.reviewers.length]
                if (reviewer.username === nextJudges[i].username) {
                  reviewer.assigned = reviewer.targetAssigned = nextJudges[i].assign
                  break
                }
              }
            }
          }
          this.tried = true
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    },
    modifyCriterion() {
      this.$http
        .post(`/api/contests/${this.contestId}/criterion`, {
          stage: this.contest.stage,
          criterion: this.criterion
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.$message({
            message: '修改评分规则成功',
            type: 'success'
          })
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    },
    refreshCriterion() {
      this.$http
        .get(`/api/contests/${this.contestId}/criterion`, {
          params: {
            stage: this.contest.stage
          }
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.criterion = resp.body.data.criterion
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    },
    refreshReview() {
      this.$http
        .get(`/api/contests/${this.contestId}/reviewtask`, {
          params: {
            stage: this.contest.stage
          }
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          let reviewers = resp.body.data
          // postprocess
          for (let reviewer of reviewers) {
            reviewer.targetAssigned = reviewer.assigned
          }
          this.reviewers = reviewers
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    },
    refreshStat() {
      this.$http
        .get(`/api/contests/${this.contestId}/taskstat`, {
          params: {
            stage: this.contest.stage
          }
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.stat = resp.body.data
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    },
    onContestChanged() {
      this.refreshReview()
      this.refreshStat()
      this.refreshCriterion()
    }
  },
  created() {
    if (this.contest.id !== -1 && !this.isNull) {
      this.onContestChanged()
    }
  },
  watch: {
    contest() {
      if (this.contest.id !== -1 && !this.isNull) {
        this.onContestChanged()
      }
    }
  }
}
</script>

<style>
</style>
