<template>
  <div>
    <button type="button" @click="init">Start</button>
    <div><canvas id="canvas"></canvas></div>
    <div id="label-container"></div>
  </div>
</template>

<script>
import * as tf from '@tensorflow/tfjs';
import * as tmPose from '@teachablemachine/pose';
// https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/pose

const URL = "../ml_files/5pose0706mlmodel/";
const modelURL = URL + "model.json";
const metadataURL = URL + "metadata.json";
let model, webcam, ctx, labelContainer, maxPredictions;
export default {
  name: "Camera1",
  props: {},
  data() {
    return {
    };
  },
  methods: {
  init(){
    // load the model and metadata
    // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
    // Note: the pose library adds a tmPose object to your window (window.tmPose)
    model = await this.tmPose.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();

    // Convenience function to setup a webcam
    const size = 200;
    const flip = true; // whether to flip the webcam
    webcam = new tmPose.Webcam(size, size, flip); // width, height, flip
    await webcam.setup(); // request access to the webcam
    await webcam.play();
    window.requestAnimationFrame(loop);

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
    await predict();
    window.requestAnimationFrame(loop);
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
