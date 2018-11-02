<template>
  <el-row align="middle" type="flex">
    <el-col :span="4"></el-col>
    <el-col :span="16">
      <el-form ref="form" :model="contest" label-width="80px">
        <el-row>
          <el-form-item label="比赛名称">
            <el-input v-model="contest.name"></el-input>
          </el-form-item>
        </el-row>
        <el-row>
          <el-form-item label="比赛学科">
            <el-input v-model="contest.subject"></el-input>
          </el-form-item>
        </el-row>
        <el-row>
          <el-form-item label="报名时间">
            <el-col :span="11">
              <el-date-picker type="date" placeholder="选择日期" v-model="contest.enrollStart" style="width: 100%;"></el-date-picker>
            </el-col>
            <el-col class="line" :span="2">-</el-col>
            <el-col :span="11">
              <el-date-picker type="date" placeholder="选择时间" v-model="contest.enrollEnd" style="width: 100%;"></el-date-picker>
            </el-col>
          </el-form-item>
        </el-row>
        <el-row>
          <el-col :span="12">
            <el-form-item label="队伍人数">
              <el-input-number v-model="contest.groupSize" :min="1" :max="10"></el-input-number>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="报名费用">
              <el-input v-model="contest.charge"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row>
          <el-form-item label="比赛描述">
            <el-input type="textarea" placeholder="请输入内容" :rows="10" v-model="contest.detail">
            </el-input>
          </el-form-item>
        </el-row>
        <el-row>
          <el-form-item label="报名网站">
            <el-col :span="6">
              使用本站提供的报名网站
              <el-checkbox v-model="useDefaultEnrollLink"></el-checkbox>
            </el-col>
            <el-col :span="6">若否，请输入报名网站链接</el-col>
            <el-col :span="6">
              <el-input v-model="contest.rrl" :disabled="useDefaultEnrollLink" placeholder="请输入内容"></el-input>
            </el-col>
          </el-form-item>
        </el-row>
        <el-row>
          <el-form-item label="比赛流程">
            <el-row>
              <el-col :span="24">
                <el-table :data="procedureList" style="width: 100%">
                  <el-table-column prop="name" label="流程名称" align="center">
                  </el-table-column>
                  <el-table-column prop="startTime" label="开始时间" align="center">
                  </el-table-column>
                  <el-table-column prop="endTime" label="结束时间" align="center">
                  </el-table-column>
                </el-table>
              </el-col>
            </el-row>
            <el-col :span="5">
              <el-input v-model="procedureName" placeholder="请输入流程名称"></el-input>
            </el-col>
            <el-col :span="1"></el-col>
            <el-col :span="6">
              <el-date-picker v-model="procedureStart" type="date" placeholder="开始日期"></el-date-picker>
            </el-col>
            <el-col :span="1"></el-col>
            <el-col :span="6">
              <el-date-picker v-model="procedureEnd" type="date" placeholder="结束日期"></el-date-picker>
            </el-col>
            <el-col :span="1"></el-col>
            <el-col :span="4">
              <el-button icon="el-icon-plus" round @click="addProcedure">添加流程</el-button>
            </el-col>
          </el-form-item>
        </el-row>
        <el-row>
          <el-form-item>
            <el-button type="primary" @click="handleCreateContest">立即创建</el-button>
          </el-form-item>
        </el-row>
      </el-form>
    </el-col>
    <el-col :span="4"></el-col>
  </el-row>
</template>
<script>
import { formatDate } from '@/lib/util'
export default {
  name: 'ContestCreate',
  data() {
    return {
      useDefaultEnrollLink: false,
      procedureList: [],
      procedureName: null,
      procedureStart: null,
      procedureEnd: null,
      contest: {
        name: null,
        subject: null,
        groupSize: null,
        enrollStart: null,
        enrollEnd: null,
        detail: null,
        procedure: null,
        url: null,
        charge: null,
        publisher: 'Aerys'
      }
    }
  },
  methods: {
    handleCreateContest() {
      if (this.useDefaultEnrollLink) this.contest.url = ''
      this.contest.enrollStart = formatDate(this.contest.enrollStart)
      this.contest.enrollEnd = formatDate(this.contest.enrollEnd)
      this.contest.procedure = JSON.stringify(this.procedureList)
      this.$http
        .post('/api/contest', this.contest, {
          emulateJSON: true
        })
        .then(function(response) {
          if (response.body.code > 0) {
            alert('Create cotnest failed with error: ' + response.body.error)
            return
          }
          this.$router.push('/contest/list')
        })
    },
    addProcedure() {
      var procedureItem = {
        name: this.procedureName,
        startTime: formatDate(this.procedureStart),
        endTime: formatDate(this.procedureEnd)
      }
      this.procedureList.push(procedureItem)
    }
  }
}
</script>