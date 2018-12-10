<template>
  <el-tabs>
    <el-tab-pane label="最热比赛">
      <contest-hot-grid></contest-hot-grid>
    </el-tab-pane>
    <el-tab-pane label="全部比赛">
      <contest-all-list></contest-all-list>
    </el-tab-pane>
  </el-tabs>
</template>
<script>
import ContestHotGrid from './ContestHotGrid.vue'
import ContestAllList from './ContestAllList.vue'

export default {
  name: 'ContestView',
  components: {
    'contest-hot-grid': ContestHotGrid,
    'contest-all-list': ContestAllList
  }
}
</script>