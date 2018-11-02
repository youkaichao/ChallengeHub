<template>
  <el-table :data="dataList">
    <el-table-column prop="fields.name" label="名称" align="center"></el-table-column>
    <el-table-column prop="fields.subject" label="学科" align="center"></el-table-column>
    <el-table-column label="详细信息" align="center">
      <template slot-scope="scope">
        <el-button type="text" @click="routeToDetail(scope.row.pk)">查看详情</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>
<script>
export default {
  name: 'ContestList',
  created: function() {
    this.$emit('onUpdateList')
  },
  methods: {
    routeToDetail(id) {
      this.$router.push(`/contest/detail/${id}`)
    }
  },
  props: ['dataList']
}
</script>