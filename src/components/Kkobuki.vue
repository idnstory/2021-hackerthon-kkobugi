<template>
  <div class="kkobuki">
    <h1>스트레칭 꼬북이</h1>
    <p>매일매일 30초 꼬북목 스트레칭 <br />같이 탈출해보자구!</p>
    <div class="img-box"></div>
    <img :src="mainImageSrc" />
    <button type="button" class="btn-start">
      <router-link to="/timer">시작하기</router-link>
    </button>
  </div>
</template>

<script>
export default {
  name: "Kkobuki",
  props: {
    msg: String
  },
  data() {
    return {
      images: [],
      mainImageSrc: null
    };
  },
  created() {
    let self = this;
    this.images = [
      {
        id: "1",
        image: require("../assets/거북남2.jpg")
      },
      {
        id: "2",
        image: require("../assets/거북교정.jpg")
      }
    ];

    setInterval(function() {
      self.mainImageSrc =
        self.images[Math.floor(Math.random() * self.images.length)].image;
    }, 300);
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  color: #42b983;
  text-decoration: none;
  font-size: 20px;
  font-weight: bold;
}
.btn-start {
  width: 500px;
  height: 50px;
  display: block;
  text-decoration: none;
  margin: 0 auto;
}
img {
  height: 678px;
}
</style>
