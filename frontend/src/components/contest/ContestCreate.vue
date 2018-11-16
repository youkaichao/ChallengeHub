<template>
  <el-form ref="form" :model="contest" label-width="100px">
    <h2>基础信息</h2>
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
      <el-form-item label="比赛图片">
        <el-input v-model="contest.imgUrl" placeholder="请填写高宽比为 3:4 的图片 url"></el-input>
      </el-form-item>
      <el-form-item label="报名网站">
        <el-col :span="6">
          <el-checkbox v-model="useDefaultEnrollLink"></el-checkbox>
          使用本站提供的报名网站
        </el-col>
        <el-col :span="6">若否，请输入报名网站链接</el-col>
        <el-col :span="6">
          <el-input v-model="contest.enrollUrl" :disabled="useDefaultEnrollLink" placeholder="请输入内容"></el-input>
        </el-col>
      </el-form-item>
    </el-row>

    <el-row>
      <h2>比赛描述</h2>
      <mavon-editor v-model="contest.detail" style="height: 800px;" />
    </el-row>

    <el-row>
      <h2>比赛流程</h2>
      <el-table :data="procedureList" style="width: 100%">
        <el-table-column prop="name" label="流程名称" align="center">
        </el-table-column>
        <el-table-column prop="startTime" label="开始时间" align="center">
        </el-table-column>
        <el-table-column prop="endTime" label="结束时间" align="center">
        </el-table-column>
      </el-table>
      <el-row :gutter="20">
        <el-col :span="6">
          <el-input v-model="procedureName" placeholder="请输入流程名称"></el-input>
        </el-col>
        <el-col :span="6">
          <el-date-picker v-model="procedureStart" type="date" placeholder="开始日期"></el-date-picker>
        </el-col>
        <el-col :span="6">
          <el-date-picker v-model="procedureEnd" type="date" placeholder="结束日期"></el-date-picker>
        </el-col>
        <el-col :span="6">
          <el-button icon="el-icon-plus" round @click="addProcedure">添加流程</el-button>
        </el-col>
      </el-row>

      <h2>自定义字段</h2>

      <el-table :data="extraFields" style="width: 100%">
        <el-table-column prop="label" label="字段名称" align="center"></el-table-column>
        <el-table-column prop="description" label="提示信息" align="center"></el-table-column>
      </el-table>
      <el-row :gutter="20">
        <el-col :span="8">
          <el-input v-model="fieldLabel" placeholder="请输入字段名称"></el-input>
        </el-col>
        <el-col :span="12">
          <el-input v-model="fieldDescription" placeholder="请输入提示信息"></el-input>
        </el-col>
        <el-col :span="4">
          <el-button icon="el-icon-plus" round @click="addField">添加字段</el-button>
        </el-col>
      </el-row>
    </el-row>
    <el-row>
      <h2>确认创建</h2>
      <el-button type="primary" @click="handleCreateContest">立即创建</el-button>
    </el-row>
  </el-form>
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
      extraFields: [],
      fieldLabel: null,
      fieldDescription: null,
      contest: {
        name: null,
        subject: null,
        groupSize: null,
        enrollStart: null,
        enrollEnd: null,
        detail: '', // set to string to use mavon-editor
        procedure: null,
        enrollForm: null,
        imgUrl: null,
        enrollUrl: null,
        charge: null,
        publisher: this.$store.state.username
      }
    }
  },
  methods: {
    async handleCreateContest() {
      if (this.useDefaultEnrollLink) this.contest.enrollUrl = ''
      this.contest.enrollStart = formatDate(this.contest.enrollStart)
      this.contest.enrollEnd = formatDate(this.contest.enrollEnd)
      this.contest.procedure = this.procedureList

      let enrollForm = {}
      for (let extraField of this.extraFields) {
        enrollForm[extraField.label] = extraField.description
      }

      this.contest.enrollForm = JSON.stringify(enrollForm)
      let response = await this.$http.post('/api/contests', this.contest)
      if (response.body.code > 0) {
        alert('Create cotnest failed with error: ' + response.body.error)
        return
      }
      this.$router.push(`/contest/detail/${response.body.data.id}`)
    },
    addProcedure() {
      var procedureItem = {
        name: this.procedureName,
        startTime: formatDate(this.procedureStart),
        endTime: formatDate(this.procedureEnd)
      }
      this.procedureList.push(procedureItem)
      this.procedureName = null
      this.procedureStart = null
      this.procedureEnd = null
    },
    addField() {
      var fieldItem = {
        label: this.fieldLabel,
        description: this.fieldDescription
      }
      this.extraFields.push(fieldItem)
      this.fieldLabel = null
      this.fieldDescription = null
    }
  }
}
</script>