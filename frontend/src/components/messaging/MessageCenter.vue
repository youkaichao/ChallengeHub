<template>
  <div>
    <el-row type="flex" justify="end">
      <el-button type="primary" @click="gotoNewMessage">给他人写私信</el-button>
    </el-row>
    <el-tabs v-model="currentTab">
      <el-tab-pane label="未读消息" name="unread">
        <el-alert
          v-if="unreadMessages.length === 0"
          title="然而并没有数据"
          type="warning"
          center
          style="width: 600px; margin: auto;"
          show-icon
        ></el-alert>
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
          @accept-reviewer-invitation="acceptReviewerInvitation"
          @reject-reviewer-invitation="rejectReviewerInvitation"
        >{{message.content}}</single-message>
      </el-tab-pane>
      <el-tab-pane label="已读消息" name="read">
        <el-alert
          v-if="readMessages.length === 0"
          title="然而并没有数据"
          type="warning"
          center
          style="width: 600px; margin: auto;"
          show-icon
        ></el-alert>
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
          @accept-reviewer-invitation="acceptReviewerInvitation"
          @reject-reviewer-invitation="rejectReviewerInvitation"
        >{{message.content}}</single-message>
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
    gotoNewMessage() {
      this.$router.push('message/new')
    },
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
      this.$router.push(`/contest/member_enroll/${contestId}/${groupId}`)
    },
    async rejectInvitation({ contestId, groupId }) {
      let response = await this.$http.post(`/apiv2/contests/${contestId}/groups/${groupId}/invitation`, {
        accept: false,
        form: ''
      })
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
    async acceptReviewerInvitation({ contestId }) {
      this.$router.push(`/contest/judge_enroll/${contestId}`)
    },
    async rejectReviewerInvitation({ contestId }) {
      let response = await this.$http.post(`/apiv2/contests/${contestId}/reviewers/response`, {
        accept: false,
        form: ''
      })
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
      let response = await this.$http.post('/apiv2/messages/delete', { id: id, type: type })
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
      await this.updateUnreadCount()
    },
    async updateReadMessages() {
      let response = await this.$http.get('/apiv2/messages', { params: { isRead: 1 } })
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }
      this.readMessages = response.body.data
      await this.updateUnreadCount()
    },
    async updateUnreadCount() {
      let response = await this.$http.get('/apiv2/messages/unread_count')
      if (response.body.code !== 0) {
        this.$message({ type: 'error', message: response.body.error })
        return
      }
      this.$store.commit('setUnreadCount', response.body.data)
    }
  }
}
</script>

<style scoped>
</style>
