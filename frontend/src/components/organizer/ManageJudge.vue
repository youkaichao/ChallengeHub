<template>
  <div>
    <el-table
      :data="judges"
      stripe
      style="width: 100%"
    >
      <el-table-column
        prop="username"
        label="用户名"
      ></el-table-column>
      <el-table-column
        prop="email"
        label="邮箱"
      ></el-table-column>
      <el-table-column
        prop="school"
        label="学校"
      ></el-table-column>
      <el-table-column label="状态">
        <template slot-scope="scope">{{scope.row.accepted === 1 ? "已接受": "未接受"}}</template>
      </el-table-column>
      <el-table-column
        v-for="(item,index) in formKeys"
        :label="item"
        :key="index"
        :prop="'enrollForm.'+item"
      ></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            v-if="scope.row.accepted === 0"
            el-button
            type="text"
            @click="removeJudge(scope.row.username)"
          >取消邀请</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-row>
      <el-col :span="5">
        <el-autocomplete
          v-model="input"
          :fetch-suggestions="querySearchAsync"
          placeholder="请输入评委用户名"
        ></el-autocomplete>
      </el-col>
      <el-col
        :span="4"
        :offset="1"
      >
        <el-button
          type="primary"
          @click="addJudge"
        >添加新评委</el-button>
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
      input: '',
      enrollForm: '[]'
    }
  },
  methods: {
    querySearchAsync(queryString, callback) {
      if (queryString) {
        this.$http
          .get('/api/users', {
            params: {
              prefix: queryString
            }
          })
          .then(resp => {
            if (resp.body.code !== 0) {
              throw new Error(resp.body.error)
            }
            let values = resp.body.data
            values = values.map(x => ({ value: x.username }))
            callback(values)
          })
          .catch(() => {})
      }
    },
    refreshEnrollForm() {
      this.$http
        .get(`/api/contests/${this.contestId}/enroll`)
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.enrollForm = resp.body.data.enrollForm
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    },
    refreshJudge() {
      this.$http
        .get(`/api/contests/${this.contestId}/reviewer`, { params: { all: 1 } })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.judges = resp.body.data
          for (let judge of this.judges) {
            judge.enrollForm = JSON.parse(judge.enrollForm)
          }
        })
        .catch(err => {
          this.$alert(err.toString())
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
          this.$alert(err.toString())
        })
    },
    async removeJudge(username) {
      let response = await this.$http.post(`/apiv2/contests/${this.contestId}/reviewers/cancel`, {
        username: username
      })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }

      this.$message({ type: 'success', message: `成功撤销邀请` })
      this.refreshJudge()
    }
  },
  computed: {
    formKeys() {
      let forms = JSON.parse(this.enrollForm)
      return forms.map(x => x.label)
    }
  },
  created() {
    this.refreshJudge()
    this.refreshEnrollForm()
  }
}
</script>

<style>
</style>
