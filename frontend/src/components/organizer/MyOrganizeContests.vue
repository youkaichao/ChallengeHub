<template>
  <div>
    <el-table :data="contests">
      <el-table-column label="比赛名称" prop="name"></el-table-column>
      <el-table-column label="学科" prop="subject"></el-table-column>
      <el-table-column label="报名开始" prop="enrollStart"></el-table-column>
      <el-table-column label="报名结束" prop="enrollEnd"></el-table-column>
      <el-table-column label="主办方" prop="publisher"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button type="text" @click="$router.push(`/organizer/${scope.row.id}`)">管理比赛</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-row>
      <el-col :span="4">
        <el-button type="primary" @click="$router.push('/contest/create')">
          创建比赛
        </el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'MyOrganizeContests',
  data() {
    return {
      contests: []
    }
  },
  created() {
    this.$http
      .get('/api/users/created', {
        params: {
          username: this.$store.state.username
        }
      })
      .then(resp => {
        this.contests = resp.body.data
      })
      .catch(err => {
        this.$alert(err)
      })
  }
}
</script>

<style>
</style>
