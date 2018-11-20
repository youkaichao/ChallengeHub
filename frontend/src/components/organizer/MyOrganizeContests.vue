<template>
  <div>
    <el-row type='flex' align-items="center">
      <el-col :span="6" style="text-align: left; margin: auto;"> <span class="info-tag">姓名</span> {{ this.$store.state.username }} </el-col>
      <el-col :span="6" style="text-align: left; margin: auto;"> <span class="info-tag">学校</span> {{ this.$store.state.school }} </el-col>
      <el-col :span="6" style="text-align: left; margin: auto;"> <span class="info-tag">邮箱</span> {{ this.$store.state.email }} </el-col>
      <el-col :span="6" style="text-align: right;">
        <el-button type="text" @click="$router.push('/user')">修改个人信息</el-button>
      </el-col>
    </el-row>

    <h1 style="font-size: 48px;">我管理的比赛</h1>

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

    <el-button type="primary" style= "margin-top: 20px;" @click="$router.push('/contest/create')">
      创建比赛
    </el-button>

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

<style scoped>
.info-tag {
  color: #409eff;
  margin-left: 10px;
  margin-right: 10px;
}
</style>
