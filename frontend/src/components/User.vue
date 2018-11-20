<template>
  <div>
    <competition-dashboard v-if="isIndividual && isCompetitor" v-on:switch-judge="isCompetitor = false" />
    <judge-dashboard v-else-if="isIndividual && !isCompetitor" v-on:switch-competitor="isCompetitor = true" />
    <my-organize-contests v-else-if="isLogin" />
    <div v-else>
      <h1>你还没有登录！</h1>
    </div>
  </div>
</template>

<script>
import CompetitorDashboard from './dashboard/CompetitorDashboard.vue'
import JudgeDashboard from './dashboard/JudgeDashboard.vue'
import MyOrganizeContests from './organizer/MyOrganizeContests.vue'

export default {
  name: 'User',
  data() {
    return {
      isCompetitor: true
    }
  },
  computed: {
    isIndividual() {
      return this.$store.state.login && this.$store.state.individual
    },
    isLogin() {
      return this.$store.state.login
    }
  },
  components: {
    'competition-dashboard': CompetitorDashboard,
    'judge-dashboard': JudgeDashboard,
    'my-organize-contests': MyOrganizeContests
  }
}
</script>