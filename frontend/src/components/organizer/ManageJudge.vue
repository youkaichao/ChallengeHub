<template>
  <div>
    <el-table :data="judges" stripe style="width: 100%">
      <el-table-column prop="username" label="用户名">
      </el-table-column>
      <el-table-column prop="email" label="邮箱">
      </el-table-column>
      <el-table-column prop="school" label="学校">
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="text" @click="removeJudge(scope.row.username)">移除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-row>
      <el-col :span="5">
        <el-input v-model="input" placeholder="请输入评委用户名"></el-input>
      </el-col>
      <el-col :span="4" :offset="1">
        <el-button type="primary" @click="addJudge">添加新评委</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'ManageJudge',
  props: ['contest', 'contestId'],
  data() {
    return {
      judges: [],
      input: ''
    }
  },
  methods: {
    refreshJudge() {
      this.$http
        .get(`/api/contests/${this.contestId}/reviewer`)
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.judges = resp.body.data
        })
        .catch(err => {
          this.$alert(err)
        })
    },
    addJudge() {
      let username = this.input
      this.input = ''
      this.$http
        .post(`/api/contests/${this.contestId}/reviewer`, {
          username: [username]
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.refreshJudge()
        })
        .catch(err => {
          this.$alert(err)
        })
    },
    removeJudge(username) {
      this.$alert('todo ' + username)
    }
  },
  created() {
    this.refreshJudge()
  }
}
</script>

<style>
</style>
