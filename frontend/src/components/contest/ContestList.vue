<template>
  <el-table :data="list" align="left">
    <el-table-column prop="name" label="名称"></el-table-column>
    <el-table-column prop="subject" label="学科"></el-table-column>
    <el-table-column label="详细信息">查看详情</el-table-column>
  </el-table>
</template>
<script>
export default {
  name: 'ContestList',
  data() {
    return {
      list: []
    }
  },
  methods: {},
  created: function() {}
}
</script>