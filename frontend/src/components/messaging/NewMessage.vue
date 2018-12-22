<template>
  <div>
    <h1>收信者名称</h1>
    <el-autocomplete
      style="width: 50%;"
      placeholder="请输入名称"
      v-model="peer"
      :fetch-suggestions="querySearchAsync"
      :disabled="peerDisabled"
    ></el-autocomplete>
    <h1>私信正文</h1>
    <el-input
      type="textarea"
      style="width: 50%;"
      :autosize="{ minRows: 20, maxRows: 80}"
      placeholder="请输入内容"
      v-model="content"
    >
    </el-input>
    <div>
      <el-button
        type="primary"
        style="margin-top: 20px;"
        @click="sendMessage"
      >发送私信</el-button>
    </div>
  </div>
</template>

<script>
export default {
  created() {
    if (this.$route.params.peer === null || this.$route.params.peer === undefined) {
      this.peer = ''
    } else {
      this.peer = this.$route.params.peer
      this.peerDisabled = true
    }
  },
  data() {
    return {
      peer: '',
      content: '',
      peerDisabled: false
    }
  },
  methods: {
    querySearchAsync(queryString, callback) {
      if (queryString) {
        this.$http
          .get('/api/users', {
            params: {
              prefix: queryString
            }
          })
          .then(resp => {
            if (resp.body.code !== 0) {
              throw new Error(resp.body.error)
            }
            let values = resp.body.data
            values = values.map(x => ({ value: x.username }))
            callback(values)
          })
          .catch(() => {})
      }
    },
    async sendMessage() {
      let response = await this.$http.post(`/apiv2/messages`, { peer: this.peer, content: this.content })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }
      this.$message({ type: 'success', message: `消息发送成功` })
      this.$router.push(`/message`)
    }
  }
}
</script>

<style>
</style>
