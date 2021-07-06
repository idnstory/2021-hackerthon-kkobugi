<template>
  <div>
    <button type="button" @click="init">Start</button>
    <div><canvas id="canvas"></canvas></div>
    <div id="label-container"></div>
  </div>
</template>

<script>
// const URL = "../ml_files/5pose0706mlmodel/";
// const modelURL = URL + "model.json";
// const metadataURL = URL + "metadata.json";
let model, webcam, ctx, labelContainer, maxPredictions;
export default {
  name: "Camera1",
  props: {},
  data() {
    return {
    };
  },
  methods: {
  init: async function(){
    // load the model and metadata
    // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
    // Note: the pose library adds a tmPose object to your window (window.tmPose)
    model = await tmPose.load("https://teachablemachine.withgoogle.com/models/Wkb2tGYGr/model.json", "https://teachablemachine.withgoogle.com/models/Wkb2tGYGr/metadata.json");
    maxPredictions = model.getTotalClasses();

    // Convenience function to setup a webcam
    const size = 200;
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
          if(maxValue < prediction[i].probability) {
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
  },
  },
  computed: {},
  watch: {

  },
  mounted() {

  }
};
</script>

<style></style>
