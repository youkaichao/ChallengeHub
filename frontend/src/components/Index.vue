<template>
  <el-row>
    <div style="font-family: 'Titillium Web'; margin-top: 100px; margin-bottom: 100px;">
      <h1>欢迎来到 <b>Challenge</b>Hub!</h1>
      <el-button type="primary" @click="$router.push('/contest/list')">查看 <b>Challenge</b>Hub 上的比赛</el-button>
    </div>
  </el-row>
</template>

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
