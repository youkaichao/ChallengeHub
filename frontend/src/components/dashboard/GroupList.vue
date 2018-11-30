<template>
  <div>
    <el-row>
      <el-col :span="12">
        <group-card
          v-for="(group,index) in groups"
          v-if="index%2==0"
          :group="group"
          :key="index"
        />
      </el-col>
      <el-col :span="12">
        <group-card
          v-if="index%2==1"
          v-for="(group,index) in groups"
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
    }
  },
  created() {
    this.refreshAllGroups()
  }
}
</script>

<style>
</style>
