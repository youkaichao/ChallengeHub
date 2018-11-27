<template>
  <el-form ref="form" :rules="rules" :model="contest" label-width="100px">
    <h2>基础信息</h2>
    <el-row>
      <el-form-item label="比赛名称" prop="contestName">
        <el-input v-model="contest.name"></el-input>
      </el-form-item>
    </el-row>
    <el-row>
      <el-form-item label="比赛学科" prop="contestSubject">
        <el-input v-model="contest.subject"></el-input>
      </el-form-item>
    </el-row>
    <el-row>
      <el-form-item label="报名时间" prop="enrollStart">
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
          <el-input-number v-model="contest.charge"></el-input-number>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row>
      <el-form-item label="比赛图片" prop="imgUrl">
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
          <el-form-item>
            <el-input v-model="procedureName" placeholder="请输入流程名称"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item>
            <el-date-picker v-model="procedureStart" type="date" placeholder="开始日期"></el-date-picker>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item>
            <el-date-picker v-model="procedureEnd" type="date" placeholder="结束日期"></el-date-picker>
          </el-form-item>
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
    let validateStartEnd = (rule, value, callback) => {
      if (!this.contest.enrollStart || !this.contest.enrollEnd) {
        callback('请输入开始和结束时间')
      } else {
        let startTime = new Date(this.contest.enrollStart)
        let endTime = new Date(this.contest.enrollEnd)
        if (startTime >= endTime) {
          callback(new Error('开始时间应小于结束时间'))
        } else {
          callback()
        }
      }
    }
    return {
      useDefaultEnrollLink: false,
      procedureList: [],
      procedureName: '',
      procedureStart: '',
      procedureEnd: '',
      extraFields: [],
      fieldLabel: '',
      fieldDescription: '',
      contest: {
        name: '',
        subject: '',
        groupSize: 1,
        enrollStart: null,
        enrollEnd: null,
        detail: '', // set to string to use mavon-editor
        procedure: [],
        enrollForm: null,
        imgUrl: '',
        enrollUrl: '',
        charge: 0,
        publisher: this.$store.state.username
      },
      rules: {
        // contestName: [{ required: true, message: '请输入比赛名称', trigger: 'blur' }]
        // contestSubject: [{ required: true, message: '请输入比赛学科', trigger: 'blur' }]
        enrollStart: [
          { type: 'date', message: '必须是一个合法的日期', trigger: 'change' },
          { validator: validateStartEnd, trigger: ['blur', 'change'] }
        ]
      }
    }
  },
  methods: {
    async handleCreateContest() {
      this.$refs['form'].validate(valid => {
        if (valid) {
          if (this.useDefaultEnrollLink) {
            this.contest.enrollUrl = ''
          } else if (!this.contest.enrollUrl) {
            this.$message.error('报名链接不能为空')
            return
          }
          if (!this.contest.name) {
            this.$message.error('比赛名称不能为空')
            return
          }
          if (!this.contest.subject) {
            this.$message.error('比赛学科不能为空')
            return
          }
          // this.contest.enrollStart = formatDate(this.contest.enrollStart)
          // this.contest.enrollEnd = formatDate(this.contest.enrollEnd)
          if (this.procedureList.length === 0) {
            this.$message.error('至少有一个比赛流程')
            return
          }
          this.contest.procedure = this.procedureList

          let enrollForm = {}
          for (let extraField of this.extraFields) {
            enrollForm[extraField.label] = extraField.description
          }

          this.contest.enrollForm = JSON.stringify(enrollForm)
          this.$http
            .post('/api/contests', this.contest)
            .then(response => {
              if (response.body.code > 0) {
                throw new Error(response.body.error)
              }
              this.$router.push(`/contest/detail/${response.body.data.id}`)
            })
            .catch(err => {
              this.$alert('Create contest failed with error: ' + err.toString())
            })
        } else {
          this.$message.error('表单有误，请修改后提交')
        }
      })
    },
    addProcedure() {
      if (!this.procedureName) {
        this.$message.error('请输入阶段名称')
        return
      }
      let isDate = function(date) {
        return new Date(date) !== 'Invalid Date' && !isNaN(new Date(date))
      }
      if (!isDate(this.procedureStart) || !isDate(this.procedureEnd)) {
        this.$message.error('请输入开始和结束时间')
        return
      }
      let start = new Date(this.procedureStart)
      let end = new Date(this.procedureEnd)
      if (start > end) {
        this.$message.error('开始时间应小于结束时间')
        return
      }
      let procedureItem = {
        name: this.procedureName,
        startTime: formatDate(this.procedureStart),
        endTime: formatDate(this.procedureEnd)
      }
      this.procedureList.push(procedureItem)
      this.procedureName = ''
      this.procedureStart = ''
      this.procedureEnd = ''
    },
    addField() {
      if (!this.fieldLabel) {
        this.$message.error('请输入字段名称')
        return
      }
      var fieldItem = {
        label: this.fieldLabel,
        description: this.fieldDescription
      }
      this.extraFields.push(fieldItem)
      this.fieldLabel = ''
      this.fieldDescription = ''
    }
  }
}
</script>
