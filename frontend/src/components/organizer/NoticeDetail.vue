<template>
  <div>
    <el-form @submit.native.prevent label-width="80px">
      <el-form-item label="公告标题">
        <el-input v-model="noticeTitle" placeholder="公告标题" width="100"></el-input>
      </el-form-item>
    </el-form>
    <mavon-editor v-model="noticeDetail" style="height: 800px;" />
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
  computed: {
    noticeId() {
      return this.$route.params.noticeId
    }
  },
  methods: {
    submitNotice() {
      this.$alert('todo')
    },
    cancelEdit() {
      this.$router.push({
        name: 'notices',
        params: {
          id: this.contestId
        }
      })
    }
  }
}
</script>

<style>
</style>
