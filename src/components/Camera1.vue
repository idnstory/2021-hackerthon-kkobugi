<template>
  <div class="my-4 container">
    <h2 class="font-50 mb-4">{{ getName }}님, 동작을 따라해보세요!</h2>
    <div class="text-right">
      <span class="font-30">스코어: {{ score }} /100</span>
    </div>
    <b-card-group deck>
      <b-row>
        <b-col>
          <b-card
            bg-variant="info"
            text-variant="white"
            header="스트레칭"
            class="text-center"
          >
            <span>{{ currentVO.text }}</span>
            <img :src="currentVO.image" class="img-loader w-100" />
          </b-card>
        </b-col>
        <b-col>
          <b-card bg-variant="light" header="카메라" class="text-center">
            <div><canvas id="canvas"></canvas></div>
            <div id="label-container"></div>
          </b-card>
        </b-col>
      </b-row>
    </b-card-group>
    <p class="font-50" :class="{ green: checkColor, danger: !checkColor }">
      결과는? {{ resultAnswer }}
    </p>
    <audio autoplay loop>
      <source src="../assets/main_theme.mp3" type="audio/mp3" />
    </audio>
  </div>
</template>
<script>
import axios from "axios";
// const URL = "../ml_files/5pose0706mlmodel/";
// const modelURL = URL + "model.json";
// const metadataURL = URL + "metadata.json";
let model, webcam, ctx, labelContainer, maxPredictions;
// const url1 = require("../../src/assets/1.jpeg");
export default {
  name: "Camera1",
  Timerprops: {},
  data() {
    return {
      imageIndex: 0,
      checkColor: true,
      resultAnswer: "",
      sucessClass: "green",
      errorClass: "danger",
      score: 0,
      imageArray: [
        {
          text: "",
          image: require("@/assets/거북남준비중1.jpg"),
          answer: "white"
        },
        {
          text: "1번자세",
          image: require("@/assets/pose1-1.png"),
          answer: "pose1"
        },
        {
          text: "2번자세",
          image: require("@/assets/pose2-1.png"),
          answer: "pose2"
        },
        {
          text: "3번자세",
          image: require("@/assets/pose3-1.png"),
          answer: "pose3"
        },
        {
          text: "4번자세",
          image: require("@/assets/pose4-1.png"),
          answer: "pose4"
        },
        {
          text: "5번자세",
          image: require("@/assets/pose5-1.png"),
          answer: "pose4"
        },
        {
          text: "6번자세",
          image: require("@/assets/pose6-1.png"),
          answer: "pose4"
        },
        {
          text: "7번자세",
          image: require("@/assets/pose7-1.png"),
          answer: "pose4"
        },
        {
          text: "8번자세",
          image: require("@/assets/pose8-1.png"),
          answer: "pose4"
        },
        {
          text: "9번자세",
          image: require("@/assets/pose9-1.png"),
          answer: "pose4"
        },
        {
          text: "10번자세",
          image: require("@/assets/pose10-1.png"),
          answer: "pose4"
        }
      ]
    };
  },
  methods: {
    init: async function() {
      // load the model and metadata
      // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
      // Note: the pose library adds a tmPose object to your window (window.tmPose)
      model = await tmPose.load(
        "https://teachablemachine.withgoogle.com/models/fAbOcVsYc/model.json",
        "https://teachablemachine.withgoogle.com/models/fAbOcVsYc/metadata.json"
      );
      maxPredictions = model.getTotalClasses();

      // Convenience function to setup a webcam
      const size = 400;
      const flip = true; // whether to flip the webcam
      webcam = new tmPose.Webcam(size, size, flip); // width, height, flip
      await webcam.setup(); // request access to the webcam
      await webcam.play();
      window.requestAnimationFrame(this.loop);

      // append/get elements to the DOM
      const canvas = document.getElementById("canvas");
      canvas.width = size;
      canvas.height = size;
      ctx = canvas.getContext("2d");
      labelContainer = document.getElementById("label-container");
      for (let i = 0; i < maxPredictions; i++) {
        // and class labels
        labelContainer.appendChild(document.createElement("div"));
      }
    },
    loop: async function(timestamp) {
      webcam.update(); // update the webcam frame
      await this.predict();
      window.requestAnimationFrame(this.loop);
    },
    predict: async function() {
      // Prediction #1: run input through posenet
      // estimatePose can take in an image, video or canvas html element
      const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
      // Prediction 2: run input through teachable machine classification model
      const prediction = await model.predict(posenetOutput);

      var maxValueClassName;
      var maxValue = 0;
      for (let i = 0; i < maxPredictions; i++) {
        const classPrediction =
          prediction[i].className + ": " + prediction[i].probability.toFixed(2);
        labelContainer.childNodes[i].innerHTML = classPrediction;
        if (maxValue < prediction[i].probability) {
          maxValue = prediction[i].probability;
          maxValueClassName = prediction[i].className;
        }
      }

      const classified = "classified";
      // console.log(maxValueClassName);
      localStorage.setItem(classified, maxValueClassName);

      // finally draw the poses
      this.drawPose(pose);
    },
    drawPose: function(pose) {
      if (webcam.canvas) {
        ctx.drawImage(webcam.canvas, 0, 0);
        // draw the keypoints and skeleton
        if (pose) {
          const minPartConfidence = 0.5;
          tmPose.drawKeypoints(pose.keypoints, minPartConfidence, ctx);
          tmPose.drawSkeleton(pose.keypoints, minPartConfidence, ctx);
        }
      }
    },
    resultMessage: function() {
      if (this.getImageAnswer === this.getItems) {
        this.resultAnswer = "GOOD!";
        this.checkColor = true;
        this.score += 10;
        console.log("정답!", this.getImageAnswer, this.getItems);
      } else {
        this.resultAnswer = "BAD";
        this.checkColor = false;
        console.log("오답!", this.getImageAnswer, this.getItems);
      }
    }
  },
  computed: {
    currentVO() {
      return this.imageArray[this.imageIndex];
    },
    getImageAnswer() {
      return this.currentVO.answer;
    },
    getItems() {
      return localStorage.getItem("classified");
    },
    getName() {
      return (this.getname = localStorage.getItem("myname"));
    }
  },
  watch: {},
  // created: {},
  beforeMount() {
    this.init();
  },
  created() {},
  mounted() {
    let intervalID = setInterval(() => {
      this.imageIndex++;
      if (this.imageIndex == this.imageArray.length) {
        axios
          .post("http://kkobuki.haezoom.io:8080/ranking/ranking/", {
            name: this.getName,
            score: this.score
          })
          .then(function(response) {
            console.log(response);
          })
          .catch(function(error) {
            console.log(error);
          });
        this.$router.push("/ranking");
        clearInterval(intervalID);
      }
      this.resultMessage();
    }, 7000);
  }
};
</script>
<style lang="scss" scoped>
.container {
  padding: 20px;
  #label-container {
    display: none !important;
  }
}
h2 {
  margin-top: 30px;
}
.text-right {
  text-align: right;
}
.danger {
  margin-top: 20px;
  color: red;
}
.green {
  margin-top: 20px;
  color: green;
}
.font {
  &-20 {
    font-size: 20px;
  }
  &-30 {
    font-size: 30px;
  }
  &-50 {
    font-size: 50px;
  }
}
.card-header {
  font-size: 30px;
}
</style>
