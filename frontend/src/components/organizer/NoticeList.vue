<template>
  <div>
    <el-table :data="notices">
      <el-table-column label="序号" prop="id"></el-table-column>
      <el-table-column label="公告标题" prop="title"></el-table-column>
      <el-table-column label="最后修改时间" prop="modifiedTime"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="text" @click="enterModify(scope.row.id)">修改</el-button>
          <el-button type="text" class="danger-text" @click="deleteNotice(scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-row>
      <el-col :span="4">
        <el-button type="primary" @click="createNewNotice">创建新公告</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      notices: []
    }
  },
  props: ['contest', 'contestId'],
  methods: {
    enterModify(id) {
      this.$router.push({
        name: 'noticedetail',
        params: {
          id: this.contestId,
          noticeId: id
        }
      })
    },
    deleteNotice(id) {
      this.$confirm('你确定要删除这条公告吗？')
        .then(() => {
          this.$http
            .delete(`/api/contests/${this.contestId}/notices/${id}`)
            .then(resp => {
              if (resp.body.code !== 0) {
                throw new Error(resp.body.error)
              }
              this.refreshNotices()
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
    createNewNotice() {
      this.$router.push({
        name: 'newnotice',
        params: {
          id: this.contestId
        }
      })
    },
    refreshNotices() {
      this.$http
        .get(`/api/contests/${this.contestId}/notices`)
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.notices = resp.body.data.notices
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    }
  },
  created() {
    this.refreshNotices()
  }
}
</script>

<style>
.danger-text {
  color: #f56c6c !important;
}
</style>
