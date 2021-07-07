<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>

<style lang="scss">
#app {
  min-width: 320px;
  max-width: 960px;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  margin: 0 auto;
  border: 1px solid #eee;
  -webkit-font-smoothing: antialiased;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  body {
    font-family: "Spoqa Han Sans", "Spoqa Han Sans JP", "Sans-serif";
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    margin: 0;
    padding: 0;
  }
}
</style>
