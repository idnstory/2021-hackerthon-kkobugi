<template>
  <div class="p-8">
    <h2>동작을 따라해보세요!</h2>
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
          <b-card
            bg-variant="light"
            text-variant="white"
            header="카메라"
            class="text-center"
          >
            <div><canvas id="canvas"></canvas></div>
            <button type="button" @click="SaveUploadImage">save canvas to image</button>
            <div id="label-container"></div>
            <input type="file" accept="image/*" @change="SaveUploadImage($event)" id="file-input">
          </b-card>
        </b-col>
      </b-row>
    </b-card-group>
  </div>
</template>
<script>
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
      imageArray: [
        {
          text: "1번자세",
          image: require("@/assets/pose1-1.png")
        },
        {
          text: "2번자세",
          image: require("@/assets/pose2-1.png")
        },
        {
          text: "3번자세",
          image: require("@/assets/pose3-1.png")
        },
        {
          text: "4번자세",
          image: require("@/assets/pose4-1.png")
        },
        {
          text: "5번자세",
          image: require("@/assets/pose5-1.png")
        },
        {
          text: "6번자세",
          image: require("@/assets/pose6-1.png")
        },
        {
          text: "7번자세",
          image: require("@/assets/pose7-1.png")
        },
        {
          text: "8번자세",
          image: require("@/assets/pose8-1.png")
        },
        {
          text: "9번자세",
          image: require("@/assets/pose9-1.png")
        },
        {
          text: "10번자세",
          image: require("@/assets/pose10-1.png")
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
    SaveUploadImage: function(){
      //save
      const canvas_img = document.getElementById("canvas")
        .toDataURL("image/jpeg")
        .replace("image/jpeg", "image/octet-stream");
      console.log(canvas_img);
      var link = document.createElement('a');
      link.download = "my-image.png";
      link.href = canvas_img;
      link.click();
      console.log("save1");

      //save2
      console.log("second upload logic");
      var imgDataUrl = document.getElementById("canvas").toDataURL('image/png');
    
      var blobBin = atob(imgDataUrl.split(',')[1]);	// base64 데이터 디코딩
      var array = [];
      for (var i = 0; i < blobBin.length; i++) {
          array.push(blobBin.charCodeAt(i));
      }
      var file = new Blob([new Uint8Array(array)], {type: 'image/png'});	// Blob 생성
      var formdata = new FormData();	// formData 생성
      formdata.append("file", file);	// file data 추가

      $.ajax({
        type : 'get',
        url : 'http://kkobuki.haezoom.io:8080/ranking/rankingtest',
        data : formdata,
        processData : false,	// data 파라미터 강제 string 변환 방지!!
        contentType : false,	// application/x-www-form-urlencoded; 방지!!
        success : function (data) {
            console.log("success transer data");
            console.log(data);
        }
        
    });
      //upload
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
      console.log(maxValueClassName);
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
    }
  },
  computed: {
    currentVO() {
      return this.imageArray[this.imageIndex];
    }
  },
  watch: {},
  // created: {},
  beforeMount() {
    this.init();
  },
  mounted() {
    let intervalID = setInterval(() => {
      this.imageIndex++;
      if (this.imageIndex == this.imageArray.length) {
        clearInterval(intervalID);
      }
    }, 5000);
  }
};
</script>
