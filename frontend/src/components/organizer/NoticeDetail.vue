<template>
  <div>
    <el-form @submit.native.prevent label-width="160px">
      <el-form-item label="公告标题">
        <el-input v-model="noticeTitle" placeholder="公告标题" width="100"></el-input>
      </el-form-item>
      <el-form-item label="上次修改时间">{{this.modifiedTime}}</el-form-item>
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
      noticeTitle: '',
      modifiedTime: ''
    }
  },
  computed: {
    noticeId() {
      return this.$route.params.noticeId
    }
  },
  methods: {
    submitNotice() {
      this.$http
        .put(`/api/contests/${this.contestId}/notices/${this.noticeId}`, {
          title: this.noticeTitle,
          content: this.noticeDetail
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.$message({
            message: '修改公告成功',
            type: 'success'
          })
          this.getNotice()
        })
        .catch(err => {
          this.$alert(err.toString())
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
    getNotice() {
      this.$http
        .get(`/api/contests/${this.contestId}/notices/${this.noticeId}`)
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.noticeTitle = resp.body.data.title
          this.noticeDetail = resp.body.data.content
          this.modifiedTime = resp.body.data.modifiedTime
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    },
    addImgHint(pos, file) {
            this.$refs.md.$img2Url(pos, file.miniurl)
      this.$alert('目前我们使用 Base64 上传图片，请在后续使用图片中尽量填写 URL。')
    }
  },
  created() {
    this.getNotice()
  }
}
</script>

<style>
</style>
