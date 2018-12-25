<template>
  <div>
    <p>创建新公告</p>
    <el-form @submit.native.prevent label-width="80px">
      <el-form-item label="公告标题">
        <el-input v-model="noticeTitle" placeholder="公告标题" width="100"></el-input>
      </el-form-item>
    </el-form>
    <mavon-editor v-model="noticeDetail" style="height: 800px;" @imgAdd="addImgHint" ref="md"/>
    <el-row>
      <el-button type="primary" @click="submitNotice">保存并提交</el-button>
      <el-button type="warning" @click="cancelEdit">放弃更改</el-button>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'NoticeDetail',
  props: ['contest', 'contestId'],
  data() {
    return {
      noticeDetail: '',
      noticeTitle: ''
    }
  },
  methods: {
    submitNotice() {
      this.$http
        .post(`/api/contests/${this.contestId}/notices`, {
          title: this.noticeTitle,
          content: this.noticeDetail
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.cancelEdit()
        })
        .catch(err => {
          this.$alert(err)
        })
    },
    cancelEdit() {
      this.$router.push({
        name: 'notices',
        params: {
          id: this.contestId
        }
      })
    },
    addImgHint(pos, file) {
            this.$refs.md.$img2Url(pos, file.miniurl)
      this.$alert('目前我们使用 Base64 上传图片，请在后续使用图片中尽量填写 URL。')
    }
  }
}
</script>

<style>
</style>
