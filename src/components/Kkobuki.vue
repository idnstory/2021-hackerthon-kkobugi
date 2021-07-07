<template>
  <div class="container">
    <h1>스트레칭 꼬북이</h1>
    <p>매일매일 30초 꼬북목 스트레칭 <br />같이 탈출해보자구!</p>
    <div class="img-box">
      <img :src="mainImageSrc" />
    </div>
    <b-button class="align-self-end" variant="outline-info" size="lg" block
      ><router-link to="/timer">시작하기</router-link></b-button
    >
    <audio autoplay loop>
      <source
        src="../assets/02 Adventure (Title Screen).mp3"
        type="audio/mp3"
      />
    </audio>
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
.container {
  position: relative;
  display: flex;
  flex-direction: column;
  padding-top: 60px;
}
a {
  width: 500px;
  color: #48c9d7;
  text-decoration: none;
  font-size: 20px;
  font-weight: bold;
  &:hover {
    color: #fff;
  }
}
button {
  display: block;
  margin: 0 auto;
  bottom: 42px;
  width: 500px;
  color: #48c9d7;
  &:hover {
    color: #fff;
  }
}
.img-box {
  height: 600px;
  margin: 0 auto;
  img {
    height: 400px;
  }
}
</style>
