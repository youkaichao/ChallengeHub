<template>
  <el-table :data="dataList" align="left">
    <el-table-column prop="name" label="名称"></el-table-column>
    <el-table-column prop="subject" label="学科"></el-table-column>
    <el-table-column label="详细信息">
      <template slot-scope="scope">
        <el-button type="text" @click="routeToDetail(scope.row.contestID)">查看详情</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>
<script>
export default {
  name: 'ContestList',
  methods: {
    routeToDetail(id) {
      this.$router.push(`/contest/detail/${id}`)
    }
  },
  props: ['dataList']
}
</script>