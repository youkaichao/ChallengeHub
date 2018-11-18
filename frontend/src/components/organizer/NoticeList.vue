<template>
  <div>
    <el-table :data="notices">
      <el-table-column label="公告标题" prop="title"></el-table-column>
      <el-table-column label="最后修改时间" prop="lastModifiedTime"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="text" @click="enterModify(scope.row.id)">修改</el-button>
          <el-button type="text" class="danger-text" @click="deleteNotice(scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-row>
      <el-col :span="4">
        <el-button type="primary" @onclick="createNewNotice">创建新公告</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      notices: [
        {
          id: 1,
          title: '公告标题',
          lastModifiedTime: '2017-1-1 12:30'
        },
        {
          id: 2,
          title: '公告标题',
          lastModifiedTime: '2017-1-1 12:30'
        }
      ]
    }
  },
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
      this.$alert('todo' + id)
    },
    createNewNotice() {
      this.$alert('todo')
    }
  }
}
</script>

<style>
.danger-text {
  color: #f56c6c !important; /*fixme*/
}
</style>
