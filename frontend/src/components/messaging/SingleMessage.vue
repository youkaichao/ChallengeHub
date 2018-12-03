<template>
  <el-card
    style="text-align: left;"
    body-style="padding: 10px;"
  >
    <div v-if="message.type === 'letter'">
      <div class="title">
        <div>
          <span>来自</span><span class="theme">{{message.sender}}</span><span>的消息</span>
        </div>
        <div class="send-date">
          <span>
            发送于 {{sendTime}}
          </span>
        </div>
      </div>
      <div class="content">
        {{message.content}}
      </div>
      <el-button
        v-if="!read"
        type="primary"
        plain
        @click="$emit('mark-as-read', {id: message.id, type: message.type})"
      >标记为已读</el-button>
      <el-button
        v-if="read"
        type="primary"
        plain
        @click="$emit('delete-message', {id: message.id, type: message.type})"
      >删除消息</el-button>
      <el-button
        type="primary"
        @click="$emit('reply-message', message.sender)"
      >回复消息</el-button>
    </div>

    <div v-if="message.type === 'system'">
      <div class="title">
        <div>
          <span class="theme">系统通知</span>
        </div>
        <div class="send-date">
          <span>
            发送于 {{sendTime}}
          </span>
        </div>
      </div>
      <div class="content">
        {{message.content}}
      </div>
      <el-button
        v-if="!read"
        type="primary"
        plain
        @click="$emit('mark-as-read', {id: message.id, type: message.type})"
      >标记为已读</el-button>
      <el-button
        v-if="read"
        type="primary"
        plain
        @click="$emit('delete-message', {id: message.id, type: message.type})"
      >删除消息</el-button>
    </div>

    <div v-if="message.type === 'invitation'">
      <div class="title">
        <div>
          <span class="theme">比赛组队邀请</span>
        </div>
        <div class="send-date">
          <span>
            发送于 {{sendTime}}
          </span>
        </div>
      </div>
      <div
        class="content"
        style="text-align: center;"
      >

        <el-card
          shadow="never"
          style="width: 600px; margin-left: auto; margin-right: auto;"
        >
          <div>
            <span class="theme bold">{{message.content.leaderName}}</span>邀请你加入<span class="theme bold">{{message.content.groupName}}</span>参加比赛<span class="theme bold">{{message.content.contestName}}</span>
          </div>
          <div style="margin-top: 20px; color: gray; font-size: 12px; margin-bottom: 10px;">
            <span v-if="message.content.status === 0">在接收邀请后，组长确认组队前，你依然可以退出</span>
            <span v-if="message.content.status === 1">你已接受这次邀请</span>
            <span v-if="message.content.status === 2">你已拒绝这次邀请</span>
            <span v-if="message.content.status === 3">这个邀请已经过期或取消</span>
          </div>

          <el-button
            type="success"
            @click="$emit('accept-invitation', {contestId: message.content.contestId, groupId: message.content.groupId})"
            v-if="message.content.status === 0"
          >接受邀请</el-button>
          <el-button
            type="danger"
            @click="$emit('reject-invitation', {contestId: message.content.contestId, groupId: message.content.groupId})"
            v-if="message.content.status === 0"
          >拒绝邀请</el-button>
        </el-card>

      </div>
      <el-button
        v-if="!read"
        type="primary"
        plain
        @click="$emit('mark-as-read', {id: message.id, type: message.type})"
      >标记为已读</el-button>
      <el-button
        v-if="read"
        type="primary"
        plain
        @click="$emit('delete-message', {id: message.id, type: message.type})"
      >删除消息</el-button>
      <el-button
        type="primary"
        plain
        @click="$emit('reply-message', message.content.leaderName)"
      >向组长发消息</el-button>
    </div>
  </el-card>
</template>

<script>
import { isoToHumanReadable } from '@/lib/util.js'

export default {
  props: ['message', 'read'],
  computed: {
    sendTime() {
      return isoToHumanReadable(this.message.sendTime)
    }
  }
}
</script>

<style scoped>
.content {
  margin-top: 15px;
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 15px;
}

.send-date {
  font-size: 12px;
}

.title {
  color: gray;
}

.bold {
  font-weight: bold;
}

.theme {
  color: #409eff;
}
</style>
