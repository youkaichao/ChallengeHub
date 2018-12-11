<template>
  <div>
    <el-alert
      title="你可以选择不同的选项对队伍进行筛选，只有满足条件的队伍会在表格中出现。"
      type="success"
    ></el-alert>
    <div style="text-align: left">
      <div
        v-for="(filterOptionsItem, index) of filterOptions"
        :key="filterOptionsItem.label"
        style="margin-top: 15px;"
      >
        <h2 style="margin-top: 5px; margin-bottom: 5px;">{{filterOptionsItem.label}}</h2>
        <el-checkbox-group v-model="filterOptions[index].selected">
          <el-checkbox
            v-for="option of filterOptionsItem.options"
            :key="option"
            :label="option"
            v-on:change="refreshGrid()"
          />
        </el-checkbox-group>
      </div>
    </div>
    <el-alert
      title="你可以在表格中搜索文本，匹配的单元格会高亮。"
      style="margin-top: 30px;"
      type="success"
    ></el-alert>
    <el-input
      v-model="searchText"
      placeholder="请输入内容以搜索"
      style="width: 400px; margin-top: 30px;"
    ></el-input>
    <el-alert
      title="你可以点击每列的标题对这些数据进行排序（可在顺序、逆序和不排序中切换）。你也可以选择部分单元格并单击右键选择复制。"
      style="margin-top: 30px;"
      type="success"
    ></el-alert>
    <div style="text-align: center; margin-top: 30px;">
      <hot-table
        ref="hot"
        :settings="settings"
        style="display: inline-block;"
      ></hot-table>
    </div>
  </div>
</template>

<script>
import { HotTable } from '@handsontable/vue'

export default {
  name: 'GroupInfo',
  props: ['contest', 'contestId'],
  async created() {
    let response = await this.$http.get(`/api/contests/${this.contestId}/groups_detail`)
    if (response.body.code !== 0) {
      this.$message({ type: 'error', message: response.body.error })
      return
    }

    this.rawData = response.body.data
    this.updateFilterOptions()
  },
  data() {
    return {
      rawData: {},
      filterOptions: [],
      searchText: '',
      settings: {
        data: [],
        colHeaders: [],
        columns: [],
        rowHeaders: true,
        width: 800,
        height: 600,
        fixedColumnsLeft: 1,
        manualColumnResize: true,
        manualRowResize: true,
        manualColumnMove: true,
        manualRowMove: true,
        stretchH: 'all',
        columnSorting: true,
        search: true,
        contextMenu: ['copy']
      }
    }
  },
  watch: {
    rawData() {
      this.refreshGrid()
    },
    searchText() {
      this.updateSearch()
    }
  },
  methods: {
    updateFilterOptions() {
      let enrollForm = JSON.parse(this.rawData.enrollForm)
      for (let item of enrollForm) {
        if (item.formType === '选择题') {
          this.filterOptions.push({
            label: item.label,
            options: item.options,
            selected: item.options
          })
        }
      }
    },
    updateSearch() {
      this.$refs.hot.hotInstance.getPlugin('search').query(this.searchText)
      this.$refs.hot.hotInstance.render()
    },
    refreshGrid() {
      let form = JSON.parse(this.rawData.enrollForm)
      let tableHeaders = ['组名']
      for (let formItem of form) {
        tableHeaders.push(formItem.label)
      }

      let tableData = []
      for (let i of this.rawData.info) {
        let name = i.name
        let answers = JSON.parse(i.form)

        // should this row be added?
        let include = true
        for (let answerItem in answers) {
          let key = answerItem
          let value = answers[key]
          for (let filterOption of this.filterOptions) {
            if (filterOption.label === key && !filterOption.selected.includes(value)) {
              include = false
              break
            }
          }
          if (!include) {
            break
          }
        }
        if (!include) {
          continue
        }

        let row = [name]
        for (let index = 1; index < tableHeaders.length; index++) {
          let label = tableHeaders[index]
          row.push(answers[label])
        }
        tableData.push(row)
      }

      this.settings.columns = Array(tableHeaders.length).fill({ readOnly: true })

      this.settings.colHeaders = tableHeaders
      this.settings.data = tableData
      this.$refs.hot.hotInstance.getPlugin('columnSorting').clearSort()
      this.updateSearch()
    }
  },
  components: {
    'hot-table': HotTable
  }
}
</script>

<style src="@/../node_modules/handsontable/dist/handsontable.full.css"></style>
<style>
</style>