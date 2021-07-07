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
@import url("https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap");
#app {
  min-width: 320px;
  max-width: 960px;
  width: 100%;
  height: 100vh;
  overflow: hidden;
  margin: 0 auto;
  border: 1px solid #eee;
  -webkit-font-smoothing: antialiased;
  font-family: "Black Han Sans", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  body {
    font-family: "Black Han Sans", sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    margin: 0;
    padding: 0;
  }
}
</style>
