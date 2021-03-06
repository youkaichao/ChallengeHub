<template>
  <div>
    <el-table :data="groups" stripe style="width: 100%" @selection-change="handleSelectionChange">
      <el-table-column type="selection"></el-table-column>
      <el-table-column prop="id" label="序号"></el-table-column>
      <el-table-column prop="name" label="队名"></el-table-column>
      <el-table-column prop="leaderName" label="队长"></el-table-column>
      <el-table-column label="队员列表">
        <template slot-scope="scope">{{ scope.row.membersName.join(', ') }}</template>
      </el-table-column>
      <el-table-column label="是否提交">
        <template slot-scope="scope">{{ scope.row.hasCommit?'已经提交':'未提交' }}</template>
      </el-table-column>
      <el-table-column prop="rank" label="奖项"></el-table-column>
      <el-table-column label="阶段">
        <template slot-scope="scope">{{ groupStageName(scope.row.stage) }}</template>
      </el-table-column>
    </el-table>
    <el-row>
      <el-button
        type="primary"
        @click="changeStage"
        :disabled="targetStage.stage===-1"
      >{{targetStage.stage === -1 ? targetStage.name : '将选中的队伍晋级至 '+targetStage.name}}</el-button>
      <el-button type="success" @click="bestowRank">给选中队伍发奖</el-button>
    </el-row>
    <el-dialog title="给选中队伍发奖" :visible.sync="centerDialogVisible" width="30%" center>
      <span>奖项的名称</span>
      <el-input v-model="rankName" placeholder="请输入奖项" style="margin: 10px"></el-input>
      <span>奖项将被颁发给以下队伍:</span>
      <span v-for="(group,index) in this.selected" :key="index">
        <span v-if="index !== 0">,</span>
        {{group.name}}
      </span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="centerDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="sendChangeRank">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
import { getGroupStage, isJudgeStage } from '@/lib/util.js'
export default {
  name: 'ManageGroup',
  props: ['contest', 'contestId'],
  data() {
    return {
      groups: [],
      selected: [],
      centerDialogVisible: false,
      rankName: ''
    }
  },
  methods: {
    handleSelectionChange(val) {
      this.selected = val
    },
    bestowRank() {
      if (this.selected.length === 0) {
        this.$alert('没有选中队伍')
        return
      }
      this.centerDialogVisible = true
    },
    sendChangeRank() {
      this.centerDialogVisible = false
      this.$http
        .post(`/api/contests/${this.contestId}/bestow`, {
          rankName: this.rankName,
          ids: this.selected.map(x => x.id)
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.reloadGroupData()
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    },
    changeStage() {
      if (this.selected.length === 0) {
        this.$alert('没有选中队伍')
        return
      }
      this.$confirm('是否将选定选手晋级？')
        .then(() => {
          let ids = this.selected.map(x => x.id)
          this.$http
            .post(`/api/contests/${this.contestId}/groups`, {
              group_ids: ids,
              stage: this.targetStage.stage
            })
            .then(resp => {
              if (resp.body.code !== 0) {
                throw new Error(resp.body.error)
              }
              this.reloadGroupData()
            })
            .catch(err => {
              this.$alert(err.toString())
            })
        })
        .catch(err => {
          if (err.toString() !== 'cancel') {
            this.$alert(err.toString())
          }
        })
    },
    reloadGroupData() {
      this.$http
        .get(`/api/contests/${this.contestId}/groups`)
        .then(resp => {
          this.groups = resp.body.data
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    },
    groupStageName(stage) {
      return getGroupStage(this.contest.procedure, stage)
    }
  },
  computed: {
    targetStage() {
      if (!isJudgeStage(this.contest.stage)) {
        return {
          name: '只有在评审阶段才能晋级选手',
          stage: -1
        }
      }
      for (let item of this.contest.procedure) {
        if (this.contest.stage + 1 === item.stage) {
          return item
        }
      }
      return {
        name: '没有下一个阶段，晋级不可用',
        stage: -1
      }
    }
  },
  created() {
    this.reloadGroupData()
  }
}
</script>

<style>
</style>
