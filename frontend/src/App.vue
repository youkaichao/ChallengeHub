<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
::-webkit-scrollbar{
display:none;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
h1 {
  font-weight: normal;
}
a {
  text-decoration: none;
  color: #000;
}
p {
  text-align: left;
  line-height: 30px;
}
.el-col {
  border: true;
  min-height: 1px;
}
.el-container {
  position: relative;
  width: 100%;
  min-height: 100%;
  padding-bottom: 100px;
  box-sizing: border-box;
}
.card-item {
  text-align: left;
  margin: 5px;
}
.el-row {
  margin: 10px;
}
.el-main {
  height: 750px;
}
.el-footer {
  position: absolute;
  bottom: 0px;
  left: 0px;
  right: 0px;
  background: #333;
}
.el-tag {
  width: 100px;
}
.my-title {
  font-weight: bolder;
  text-align: left;
  border-left: 4px solid #20a0ff;
  padding: 10px;
  line-height: 16px;
}
</style>
