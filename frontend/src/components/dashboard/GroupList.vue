<template>
  <div>
    <el-row>
      <el-col :span="12">
        <group-card
          v-for="(group,index) in evenGroups"
          :group="group"
          :key="index"
        />
      </el-col>
      <el-col :span="12">
        <group-card
          v-for="(group,index) in oddGroups"
          :group="group"
          :key="index"
        />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import GroupCard from '@/components/dashboard/GroupCard'
export default {
  name: 'GroupList',
  components: {
    'group-card': GroupCard
  },
  data() {
    return {
      groups: []
    }
  },
  methods: {
    refreshAllGroups() {
      this.$http
        .get(`/apiv2/contests/${this.contestId}/groups`)
        .then(resp => {
          if (resp.body.code !== 0) {
            throw new Error(resp.body.error)
          }
          this.groups = resp.body.data
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
    oddGroups() {
      return this.groups.filter((_, index) => index % 2 === 1)
    },
    evenGroups() {
      return this.groups.filter((_, index) => index % 2 === 0)
    }
  },
  created() {
    this.refreshAllGroups()
  }
}
</script>

<style>
</style>
