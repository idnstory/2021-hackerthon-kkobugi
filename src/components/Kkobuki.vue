<template>
  <div class="container">
    <h1>스트레칭 꼬북이</h1>
    <p>매일매일 30초 꼬북목 스트레칭 <br />같이 탈출해보자구!</p>
    <div class="img-box">
      <img :src="mainImageSrc" />
    </div>
    <b-button class="align-self-end" variant="outline-info"><router-link to="/timer">시작하기</router-link></b-button >
  <audio autoplay loop> <source src="../assets/02 Adventure (Title Screen).mp3" type="audio/mp3"> </audio>
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
        image: require("../assets/거북교정2.jpg")
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
<style scoped lang="scss">
a {
  color: #0dcaf0;
  text-decoration: none;
  font-size: 20px;
  font-weight: bold;
  &:hover {
    color: #fff;
  }
}
.btn-start {
  width: 500px;
  height: 50px;
  display: block;
  text-decoration: none;
  margin: 0 auto;
}
.img-box {
  margin: 0 auto;
  img {
    height: 400px;
  }
}
</style>
