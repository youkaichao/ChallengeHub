<template>
  <div>
    <el-card class="box-card" style="width: 800px; margin: auto;">
      <div slot="header" class="clearfix">
        <span>{{teamInfo.teamName}}</span>
      </div>

      <el-form :model="teamInfo" label-width="100px" style="width: 500px; margin: auto;">
        <h2>队伍信息</h2>
        <el-form-item
          label="队名"
          style="border-bottom: 1px solid #ebeef5; margin-bottom: 0; margin-top: 0;"
        >
          <div>{{teamInfo.teamName}}</div>
        </el-form-item>
        <el-form-item
          label="队长"
          style="border-bottom: 1px solid #ebeef5; margin-bottom: 0; margin-top: 0;"
        >
          <div>{{teamInfo.leader}}</div>
        </el-form-item>
        <el-form-item label="队员" style="margin-bottom: 0; margin-top: 0;">
          <div v-for="(member,index) in teamInfo.members" :key="index">{{member}}</div>
        </el-form-item>
        <h2>邀请管理</h2>
        <div v-for="(invitee,index) in teamInfo.invitees" :key="index" style="margin: auto;">
          <span style="margin-right: 20px;">{{invitee}}</span>
          <el-button
            type="text"
            icon="el-icon-remove"
            @click="removeInvitation(invitee)"
            :disabled="!canOperate"
          >取消邀请</el-button>
        </div>
      </el-form>
    </el-card>
    <el-row>
      <el-autocomplete
        v-model="userInput"
        :fetch-suggestions="querySearchAsync"
        placeholder="输入用户名来搜索"
      ></el-autocomplete>
      <el-button type="primary" @click="addNewMember" style="margin-left: 20px;" :disabled="!canOperate">邀请用户加入队伍</el-button>
    </el-row>
    <el-row>
      <el-button type="warning" @click="lockGroup" :disabled="!canOperate">锁定队伍</el-button>
      <el-button type="danger" @click="quitGroup" :disabled="!canOperate">退出队伍</el-button>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'GroupDashboard',
  data() {
    return {
      userInput: '',
      teamInfo: {
        teamId: -1,
        teamName: '',
        leader: '',
        members: [],
        invitees: [],
        locked: false
      }
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
    addNewMember() {
      let username = this.userInput
      this.userInput = ''
      this.$http
        .post(`/apiv2/contests/${this.contestId}/groups/${this.teamInfo.teamId}/invitenew`, {
          username
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.refreshTeamInfo()
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    },
    lockGroup() {
      this.$confirm('你确定要锁定队伍吗？锁定后队伍可以提交文件，不能再修改队伍').then(() => {
        this.$http
          .post(`/apiv2/contests/${this.contestId}/groups/${this.teamInfo.teamId}/lock`)
          .then(resp => {
            if (resp.body.code !== 0) {
              throw new Error(resp.body.error)
            }
            this.refreshTeamInfo()
          })
          .catch(err => {
            this.$alert(err.toString())
          })
      })
    },
    quitGroup() {
      let message = '你确定要退出队伍吗？'
      if (this.isLeader) {
        if (this.teamInfo.members.length === 0) {
          message += '这个队伍会被解散'
        } else {
          message += '其中一位组员会成为组长'
        }
      }
      this.$confirm(message).then(() => {
        this.$http
          .post(`/apiv2/contests/${this.contestId}/groups/${this.teamInfo.teamId}/quit`)
          .then(resp => {
            if (resp.body.code !== 0) {
              throw new Error(resp.body.error)
            }
            this.$router.push({
              name: '/user'
            })
          })
          .catch(err => {
            this.$alert(err.toString())
          })
      })
    },
    removeInvitation(username) {
      this.$confirm('真的要移除这个邀请吗？').then(() => {
        this.$http
          .post(`/apiv2/contests/${this.contestId}/groups/${this.teamInfo.teamId}/cancel`, {
            username
          })
          .then(resp => {
            if (resp.body.code !== 0) {
              throw new Error(resp.body.error)
            }
            this.refreshTeamInfo()
          })
          .catch(err => {
            this.$alert(err.toString())
          })
      })
    },
    refreshTeamInfo() {
      this.$http
        .get(`/apiv2/contests/${this.contestId}/groups`, {
          params: {
            username: this.$store.state.username
          }
        })
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          let teams = resp.body.data
          if (!teams || teams.length !== 1) {
            throw new Error('get team failed')
          }
          this.teamInfo = teams[0]
        })
        .catch(err => {
          this.$alert(err.toString())
        })
    }
  },
  computed: {
    contestId() {
      return this.$route.params.id
    },
    isLeader() {
      return this.$store.state.username === this.teamInfo.leader
    },
    canOperate() {
      return this.isLeader && !this.teamInfo.locked
    }
  },
  created() {
    this.refreshTeamInfo()
  }
}
</script>

<style>
</style>
