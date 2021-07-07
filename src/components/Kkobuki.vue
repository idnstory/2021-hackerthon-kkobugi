<template>
  <div class="container">
    <h1 class="font-60">스트레칭 꼬북이</h1>
    <p class="font-30">
      매일매일 30초 꼬북목 스트레칭 <br />같이 탈출해보자구!
    </p>
    <div class="img-box">
      <img :src="mainImageSrc" />
    </div>
    <h2>
      <span class="color-skyblue">{{ myname }}님 </span> Hi
    </h2>
    <b-button
      class="align-self-end"
      variant="outline-info"
      size="lg"
      to="/timer"
      block
      >시작하기</b-button
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
    const nameList = [
      "전지현",
      "강동원",
      "뷔",
      "정국",
      "수지",
      "조정석",
      "유재석",
      "정유미",
      "아이유",
      "박진영",
      "해줌왕",
      "박나래",
      "이영자",
      "강호동",
      "이쁨폭팔",
      "잘생김",
      "송은이",
      "이경규",
      "이효리",
      "아이티짱",
      "쌈디",
      "화사",
      "지민",
      "진",
      "제이홉",
      "RM",
      "천재",
      "차은우",
      "KCM님",
      "주먹왕랄프"
    ];
    this.myname = nameList[Math.floor(Math.random() * nameList.length)];
    const myname = "myname";
    // console.log(maxValueClassName);
    localStorage.setItem(myname, this.myname);
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
.color-skyblue {
  color: #0dcaf0;
}
h2 {
  top: -178px;
  position: relative;
  display: block;
  font-size: 32px;
}
.font {
  &-20 {
    font-size: 20px;
  }
  &-30 {
    font-size: 30px;
    line-height: 1.2;
  }
  &-60 {
    font-size: 60px;
  }
}
a {
  display: block;
  margin: 0 auto;
  width: 100%;
  bottom: 42px;
  width: 500px;
  font-size: 30px;
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
