<template>
  <el-row>
    <el-form ref="form" :model="competition" label-width="80px">
      <el-form-item label="比赛名称">
        <el-input v-model="competition.name"></el-input>
      </el-form-item>
      <el-form-item label="比赛学科">
        <el-input v-model="competition.subject"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="create">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
    <template>
      <el-table :data="list" align="left">
        <el-table-column prop="fields.name" label="名称"></el-table-column>
        <el-table-column prop="fields.subject" label="学科"></el-table-column>
      </el-table>
    </template>
  </el-row>
</template>
<script>
export default {
  name: "NewCompetition",
  data(){
    return {
      competition: {
        name: null,
        subject: null,
      },
      list: []
    }
  },
  methods:{
    create(){
      let self = this
      this.$http.post('api/add_competition', this.competition,{emulateJSON: true})
        .then((response)=>{
          if(response.body['err'] == 0){
            console.log("Success")
            self.update()
          }
          else{
            console.log("Failed wtih error: " + response.body['msg'])
          }
        }, (response)=>{
          console.log("Failed")
        })
    },
    update(){
      let self = this
      this.$http.get('api/show_competition',{},{emulateJSON: true})
        .then(function(response){
          console.log(response.body)
          self.list = response.body.list
      });
    }
  }
}
</script>
<style>
</style>