<template>
  <el-card style="margin:8px;">
    <template>
      <el-button
        v-if="group.locked"
        type="text"
        style="color:#F56C6C;"
      >
        <font-awesome-icon
          :icon="['fas','lock']"
          size="lg"
          style="margin-right:10px;"
        />{{group.teamName}}</el-button>
      <el-button
        v-else
        type="text"
        style="color:#67C23A;"
      >
        <font-awesome-icon
          :icon="['fas','lock-open']"
          size="lg"
          style="margin-right:10px;"
        />{{group.teamName}}</el-button>
    </template>
    <el-tooltip
      :content="group.leader"
      placement="top"
    >
      <el-button
        type="primary"
        circle
      >
        <font-awesome-icon
          :icon="['fas','user']"
          size="lg"
        />
      </el-button>
    </el-tooltip>
    <el-tooltip
      v-for="(member,index) in group.members"
      :key="index"
      :content="member"
      placement="top"
    >
      <el-button
        type="success"
        circle
        plain
      >
        <font-awesome-icon
          :icon="['fas','user']"
          size="lg"
        />
      </el-button>
    </el-tooltip>
    <el-tooltip
      v-for="(invitee,index) in group.invitees"
      :key="index"
      :content="invitee"
      placement="top"
    >
      <el-button
        type="info"
        circle
        plain
      >
        <font-awesome-icon
          :icon="['fas','user']"
          size="lg"
        />
      </el-button>
    </el-tooltip>
    <el-button
      style="float: right; padding: 3px 0"
      type="text"
      @click="gotoMessage()"
      icon="el-icon-message"
    >给队长发私信</el-button>
  </el-card>
</template>

<script>
export default {
  name: 'GroupCard',
  props: ['group'],
  methods: {
    gotoMessage() {
      this.$router.push(`/message/new/${this.group.leader}`)
    }
  }
}
</script>

<style>
</style>
