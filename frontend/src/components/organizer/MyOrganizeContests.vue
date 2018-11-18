<template>
  <div>
    <el-table :data="contests">
      <el-table-column label="比赛名称" prop="name"></el-table-column>
      <el-table-column label="学科" prop="subject"></el-table-column>
      <el-table-column label="报名开始" prop="enrollStart">
        <template slot-scope="scope">
          {{ isoToHumanReadable(scope.row.enrollStart) }}
        </template>
      </el-table-column>
      <el-table-column label="报名结束" prop="enrollEnd">
        <template slot-scope="scope">
          {{ isoToHumanReadable(scope.row.enrollEnd) }}
        </template>
      </el-table-column>
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
import { isoToHumanReadable } from '@/lib/util'
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
        this.$alert(err.toString())
      })
  },
  methods: {
    isoToHumanReadable
  }
}
</script>

<style>
</style>
