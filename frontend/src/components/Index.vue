<template>
  <el-row>
    <div style="font-family: 'Titillium Web'; margin-top: 100px; margin-bottom: 100px;">
      <h1>欢迎来到
        <b>Challenge</b>Hub!
      </h1>
      <el-button v-if="!$store.state.login" type="primary" @click="$router.push('/contest/list')">查看
        <b>Challenge</b>Hub 上的比赛
      </el-button>
      <div v-else>
        正在跳转到你的主页
      </div>
    </div>
  </el-row>
</template>

<script>
export default {
  created() {
    if (this.$store.state.login) {
      this.$router.push('/user')
    }
  }
}
</script>


<style>
@font-face {
  font-family: 'Titillium Web';
  src: url('../../fonts/TitilliumWeb-ExtraLight.ttf') format('truetype');
  font-weight: 100;
}

@font-face {
  font-family: 'Titillium Web';
  src: url('../../fonts/TitilliumWeb-SemiBold.ttf') format('truetype');
  font-weight: 800;
}
</style>
