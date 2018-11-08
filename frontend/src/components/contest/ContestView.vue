<template>
  <el-tabs>
    <el-tab-pane label="最热比赛">
      <transition name="el-fade-in-linear">
        <contest-hot-grid></contest-hot-grid>
      </transition>
    </el-tab-pane>
    <el-tab-pane label="全部比赛">
      <transition anme="el-fade-in-linear">
        <contest-all-list></contest-all-list>
      </transition>
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