<template>
  <div>
    <el-tabs v-model="currentTab">
      <el-tab-pane
        label="未读消息"
        name="unread"
      >
        <single-message
          v-for="message of unreadMessages"
          :key="message.id"
          :message="message"
          :read="false"
          style="margin-bottom: 30px;"
          @mark-as-read="markAsRead"
          @reply-message="replyMessage"
          @accept-invitation="acceptInvitation"
          @reject-invitation="rejectInvitation"
        >
          {{message.content}}
        </single-message>
      </el-tab-pane>
      <el-tab-pane
        label="已读消息"
        name="read"
      >
        <single-message
          v-for="message of readMessages"
          :key="message.id"
          :message="message"
          :read="true"
          style="margin-bottom: 30px;"
          @delete-message="deleteMessage"
          @reply-message="replyMessage"
          @accept-invitation="acceptInvitation"
          @reject-invitation="rejectInvitation"
        >
          {{message.content}}
        </single-message>
      </el-tab-pane>
    </el-tabs>

  </div>
</template>

<script>
import SingleMessage from './SingleMessage'

export default {
  name: 'MessageCenter',
  async created() {
    await this.updateUnreadMessages()
  },
  data() {
    return {
      unreadMessages: [],
      readMessages: [],
      currentTab: 'unread'
    }
  },
  components: {
    'single-message': SingleMessage
  },
  watch: {
    async currentTab() {
      if (this.currentTab === 'unread') {
        await this.updateUnreadMessages()
      } else {
        await this.updateReadMessages()
      }
    }
  },
  methods: {
    async markAsRead({ id, type }) {
      let response = await this.$http.put('/apiv2/messages', { id: id, type: type })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }
      let index = null
      for (let i = 0; i < this.unreadMessages.length; i++) {
        if (this.unreadMessages[i].id === id) {
          index = i
        }
      }
      if (index === null) {
        this.$message({ type: 'error', message: 'Error' })
        return
      }
      this.unreadMessages.splice(index, 1)
      this.$store.commit('decreaseUnreadCount')
    },
    async replyMessage(peerName) {
      this.$router.push(`/message/new/${peerName}`)
    },
    async acceptInvitation({ contestId, groupId }) {
      let response = await this.$http.post(`/apiv2/contests/${contestId}/groups/${groupId}/invitation`, { accept: true })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }
      this.$message({ type: 'success', message: '邀请已接受' })
      if (this.currentTab === 'unread') {
        await this.updateUnreadMessages()
      } else {
        await this.updateReadMessages()
      }
    },
    async rejectInvitation({ contestId, groupId }) {
      let response = await this.$http.post(`/apiv2/contests/${contestId}/groups/${groupId}/invitation`, { accept: false })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }
      this.$message({ type: 'success', message: '邀请已拒绝' })
      if (this.currentTab === 'unread') {
        await this.updateUnreadMessages()
      } else {
        await this.updateReadMessages()
      }
    },
    async deleteMessage({ id, type }) {
      let response = await this.$http.delete('/apiv2/messages', { params: { id: id, type: type } })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }
      let index = null
      for (let i = 0; i < this.readMessages.length; i++) {
        if (this.readMessages[i].id === id) {
          index = i
        }
      }
      if (index === null) {
        this.$message({ type: 'error', message: 'Error' })
        return
      }
      this.readMessages.splice(index, 1)
    },
    async updateUnreadMessages() {
      let response = await this.$http.get('/apiv2/messages', { params: { isRead: 0 } })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }
      this.unreadMessages = response.body.data
    },
    async updateReadMessages() {
      let response = await this.$http.get('/apiv2/messages', { params: { isRead: 1 } })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }
      this.readMessages = response.body.data
    }
  }
}
</script>

<style scoped>
</style>
