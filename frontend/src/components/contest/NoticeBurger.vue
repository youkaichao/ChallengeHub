<template>
  <div>
    <el-card :body-style="{ 'text-align': 'left', padding: '10px' }">
      <h1 style="margin-top: 0px; margin-bottom: 15px;">{{notice.title}}</h1>
      <div class="flex-box">
        <el-button type="text" style="padding: 0px;" @click="handleDetailClick">查看详情</el-button>
        <span>
          <span style="color: #409eff; margin-right: 5px;">最后更新时间</span>
          {{readableModifiedTime}}
        </span>
      </div>
    </el-card>

    <el-dialog :title="notice.title" :visible.sync="detailVisible">
      <mavon-editor
        v-model="noticeContent"
        :editable="false"
        :defaultOpen="'preview'"
        :subfield="false"
        :toolbarsFlag="false"
      />
      <el-button type="primary" style="margin-top: 20px;" @click="detailVisible = false">关闭</el-button>
    </el-dialog>
  </div>
</template>

<script>
import { isoToHumanReadable } from '@/lib/util.js'

export default {
  name: 'NoticeBurger',
  props: ['notice', 'competitionId'],
  data() {
    return {
      detailVisible: false,
      noticeContent: ''
    }
  },
  methods: {
    async handleDetailClick() {
      let response = await this.$http.get(`/api/contests/${this.competitionId}/notices/${this.notice.id}`)
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }

      this.noticeContent = response.body.data.content
      this.detailVisible = true
    }
  },
  computed: {
    readableModifiedTime() {
      return isoToHumanReadable(this.notice.modifiedTime)
    }
  }
}
</script>

<style scoped>
.flex-box {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
</style>
