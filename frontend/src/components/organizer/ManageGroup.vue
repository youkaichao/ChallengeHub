<template>
  <div>
    <el-table :data="groups" stripe style="width: 100%" @selection-change="handleSelectionChange">
      <el-table-column type="selection"></el-table-column>
      <el-table-column prop="id" label="序号">
      </el-table-column>
      <el-table-column prop="name" label="队名">
      </el-table-column>
      <el-table-column prop="leaderName" label="队长名字">
      </el-table-column>
      <el-table-column prop="rank" label="排名">
      </el-table-column>
      <el-table-column label="阶段">
        <template slot-scope="scope">{{ getStageString(scope.row.stage) }}</template>
      </el-table-column>
    </el-table>
    <el-row>
      <el-col :span="4">
        <el-select v-model="targetStage" placeholder="0">
          <el-option label="尚未开始" :value="0"></el-option>
          <el-option v-for="(stage,index) in procedureList" :key="index" :label="stage.name" :value="index+1"></el-option>
          <el-option label="已经结束" :value="-1"></el-option>
        </el-select>
      </el-col>
      <el-col :span="4" :offset="1">
        <el-button type="primary" @click="changeStage">将选中的队伍改变至阶段</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'ManageGroup',
  props: ['contest', 'procedureList', 'contestId'],
  data() {
    return {
      groups: [],
      selected: [],
      targetStage: 0
    }
  },
  methods: {
    getStageString(number) {
      if (number === 0) {
        return '尚未开始'
      } else if (number === -1) {
        return '已经结束'
      } else {
        return this.procedureList[number - 1].name
      }
    },
    handleSelectionChange(val) {
      this.selected = val
    },
    changeStage() {
      if (this.selected.length === 0) {
        this.$alert('没有选中队伍')
        return
      }
      let ids = this.selected.map(x => x.id)
      this.$http
        .post(`/api/contests/${this.contestId}/groups`, {
          group_ids: ids,
          stage: this.targetStage
        })
        .then(
          () => {
            this.reloadGroupData()
          },
          err => {
            alert(err)
          }
        )
    },
    reloadGroupData() {
      this.$http.get(`/api/contests/${this.contestId}/groups`).then(resp => {
        this.groups = resp.body.data
      })
    }
  },
  mounted() {
    this.reloadGroupData()
  }
}
</script>

<style>
</style>
