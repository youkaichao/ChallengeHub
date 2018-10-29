<template>
  <el-row align="middle" type="flex">
    <el-col :span="4"></el-col>
    <el-col :span="16">
      <el-form ref="form" :model="contest" label-width="80px">
        <el-form-item label="比赛名称">
          <el-input v-model="contest.name"></el-input>
        </el-form-item>
        <el-form-item label="比赛学科">
          <el-input v-model="contest.subject"></el-input>
        </el-form-item>
        <el-form-item label="报名时间">
          <el-col :span="11">
            <el-date-picker type="date" placeholder="选择日期" v-model="contest.enrollStartDate" style="width: 100%;"></el-date-picker>
          </el-col>
          <el-col class="line" :span="2">-</el-col>
          <el-col :span="11">
            <el-date-picker type="date" placeholder="选择时间" v-model="contest.enrollEndDate" style="width: 100%;"></el-date-picker>
          </el-col>
        </el-form-item>
        <el-form-item label="比赛时间">
          <el-col :span="11">
            <el-date-picker type="date" placeholder="选择日期" v-model="contest.competeStartDate" style="width: 100%;"></el-date-picker>
          </el-col>
          <el-col class="line" :span="2">-</el-col>
          <el-col :span="11">
            <el-date-picker type="date" placeholder="选择时间" v-model="contest.competeEndDate" style="width: 100%;"></el-date-picker>
          </el-col>
        </el-form-item>
        <el-form-item label="队伍人数">
          <el-input-number v-model="contest.memberNumber" :min="1" :max="10"></el-input-number>
        </el-form-item>
        <el-form-item label="比赛描述">
          <el-input type="textarea" placeholder="请输入内容" :rows="10" v-model="contest.description">
          </el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="handleCreateContest">立即创建</el-button>
        </el-form-item>
      </el-form>
    </el-col>
    <el-col :span="4"></el-col>
  </el-row>
</template>
<script>
export default {
  name: 'ContestCreate',
  data() {
    return {
      contest: {
        name: null,
        subject: null,
        enrollStartDate: null,
        enrollEndDate: null,
        competeStartDate: null,
        competeEndDate: null,
        memberNumber: null,
        description: null
      }
    }
  },
  methods: {
    handleCreateContest() {}
  }
}
</script>