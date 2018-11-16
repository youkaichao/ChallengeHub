<template>
  <el-container>
    <el-header height="auto">
      <el-card class="box-card">
        <div slot="header">
          <span>{{contest.name}}</span>
        </div>
        <el-tag>{{'学科: '+contest.subject}}</el-tag>
        <el-tag>{{'队伍人数: '+contest.groupSize}}</el-tag>
        <el-tag>{{'举办方: '+contest.publisher}}</el-tag>
        <el-tag>{{'报名开始时间: '+contest.enrollStart}}</el-tag>
        <el-tag>{{'报名结束时间: '+contest.enrollEnd}}</el-tag>
      </el-card>
    </el-header>
    <el-container>
      <el-aside>
        <el-menu :default-active="activeIndex" class="el-menu-vertical-demo">
          <el-menu-item index="1" @click="$router.push(`/organizer/controlpanel/${contestId}`)">比赛总览
          </el-menu-item>
          <el-menu-item index="2" @click="$router.push(`/organizer/controlpanel/${contestId}/managegroup`)">管理报名队伍
          </el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <router-view :contest="contest" :procedureList="procedureList" :contestId="contestId" @refreshContest="refreshContest"></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import ManageGroup from '@/components/organizer/ManageGroup'
import Overview from '@/components/organizer/Overview'
export default {
  name: 'ControlPanel',
  async created() {
    this.contestId = this.$route.params.id
    this.refreshContest()
  },
  data() {
    return {
      contest: null,
      contestId: null,
      procedureList: []
    }
  },
  methods: {
    refreshContest() {
      this.$http.get(`/api/contests/${this.contestId}`).then(resp => {
        this.contest = resp.body.data
        this.procedureList = this.contest.procedure
      })
    }
  },
  computed: {
    activeIndex() {
      if (this.$route.matched.length > 0) {
        let lastName = this.$route.matched[this.$route.matched.length - 1].components.default
        switch (lastName) {
          case ManageGroup:
            return '2'
          case Overview:
            return '1'
          default:
            return '1'
        }
      } else {
        return '1'
      }
    }
  }
}
</script>
<style>
.el-tag {
  width: auto;
  margin: 5px;
}
</style>
