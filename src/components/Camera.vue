<template>
  <div class="container py-4">
    <transition
      :duration="{ enter: 500, leave: 300 }"
      enter-active-class="animated zoomIn"
      leave-active-class="animated zoomOut"
      mode="out-in"
    >
    </transition>
    <h2>동작을 따라해보세요!</h2>
    <span>진행상황 progressbar?</span>
    <!--progress-->
    <div class="progressContainer">
      <!-- <progress
        class="progress is-info is-small"
        :value="(questionIndex / questions.length) * 100"
        max="100"
        >{{ (questionIndex / questions.length) * 100 }}%</progress
      > -->
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
            <li v-for="item in questions" v-bind:key="item.index">
              <span>{{ item.text }}</span>
              <img :src="item.image" class="w-100" />
            </li>
          </b-card>
        </b-col>
        <b-col>
          <b-card
            bg-variant="light"
            text-variant="white"
            header="카메라"
            class="text-center"
          >
            <div class="web-camera-container">
              <div class="camera-button">
                <b-button
                  class="button is-rounded"
                  :class="{
                    'is-primary': !isCameraOpen,
                    'is-danger': isCameraOpen
                  }"
                  @click="toggleCamera"
                >
                  <span v-if="!isCameraOpen">카메라켜기</span>
                  <span v-else>카메라끄기</span>
                </b-button>
              </div>

              <div v-show="isCameraOpen && isLoading" class="camera-loading">
                <ul class="loader-circle">
                  <li></li>
                  <li></li>
                  <li></li>
                </ul>
              </div>

              <div
                v-if="isCameraOpen"
                v-show="!isLoading"
                class="camera-box"
                :class="{ flash: isShotPhoto }"
              >
                <div
                  class="camera-shutter"
                  :class="{ flash: isShotPhoto }"
                ></div>

                <video
                  v-show="!isPhotoTaken"
                  ref="camera"
                  :height="337.5"
                  autoplay
                ></video>

                <canvas
                  v-show="isPhotoTaken"
                  id="photoTaken"
                  ref="canvas"
                  :height="337.5"
                ></canvas>
              </div>

              <div v-if="isCameraOpen && !isLoading" class="camera-shoot">
                <button type="button" class="button" @click="takePhoto">
                  <img
                    src="https://img.icons8.com/material-outlined/50/000000/camera--v2.png"
                  />
                </button>
              </div>

              <div v-if="isPhotoTaken && isCameraOpen" class="camera-download">
                <a
                  id="downloadPhoto"
                  download="kkobugi.jpg"
                  class="button"
                  role="button"
                  @click="downloadImage"
                >
                  내포즈 자랑하기
                </a>
              </div>
            </div>
          </b-card>
        </b-col>
      </b-row>
    </b-card-group>
    <!-- <b-button
      class="button"
      :class="userResponses[questionIndex] == null ? '' : 'is-active'"
      v-on:click="next()"
      :disabled="questionIndex >= questions.length"
    >
      {{ userResponses[questionIndex] == null ? "Skip" : "Next" }}
    </b-button> -->
  </div>
</template>

<script>
export default {
  name: "Camera",
  props: {},
  data() {
    return {
      questionIndex: 0,
      userResponses: this.userResponseSkelaton,
      isCameraOpen: false,
      isPhotoTaken: false,
      isShotPhoto: false,
      isLoading: false,
      link: "#",
      questions: [
        {
          text: "1번자세",
          image: require("../../src/assets/1.png")
        },
        {
          text: "HTML document start and end with which tag pairs?",
          responses: [
            { text: "HTML", correct: true },
            { text: "WEB" },
            { text: "HEAD" },
            { text: "BODY" }
          ]
        }
      ]
    };
  },
  computed: {
    userResponseSkelaton() {
      return Array(this.questions.length).fill(null);
    }
  },
  methods: {
    // restart() {
    //   this.questionIndex = 0;
    //   this.userResponses = Array(this.questions.length).fill(null);
    // }
    // score() {
    //   var score = 0;
    //   for (let i = 0; i < this.userResponses.length; i++) {
    //     if (window.CP.shouldStopExecution(0)) break;
    //     if (
    //       typeof this.questions[i].responses[this.userResponses[i]] !==
    //         "undefined" &&
    //       this.questions[i].responses[this.userResponses[i]].correct
    //     ) {
    //       score = score + 1;
    //     }
    //   }
    //   window.CP.exitedLoop(0);
    //   return score;
    // }
    toggleCamera() {
      if (this.isCameraOpen) {
        this.isCameraOpen = false;
        this.isPhotoTaken = false;
        this.isShotPhoto = false;
        this.stopCameraStream();
      } else {
        this.isCameraOpen = true;
        this.createCameraElement();
      }
    },

    createCameraElement() {
      this.isLoading = true;

      const constraints = (window.constraints = {
        audio: false,
        video: true
      });

      navigator.mediaDevices.getUserMedia(constraints).then(stream => {
        this.isLoading = false;
        this.$refs.camera.srcObject = stream;
      });
      // .catch(error => {
      //   this.isLoading = false;
      //   alert("May the browser didn't support or there is some errors.");
      // });
    },

    stopCameraStream() {
      let tracks = this.$refs.camera.srcObject.getTracks();

      tracks.forEach(track => {
        track.stop();
      });
    },

    takePhoto() {
      if (!this.isPhotoTaken) {
        this.isShotPhoto = true;

        const FLASH_TIMEOUT = 50;

        setTimeout(() => {
          this.isShotPhoto = false;
        }, FLASH_TIMEOUT);
      }

      this.isPhotoTaken = !this.isPhotoTaken;

      const context = this.$refs.canvas.getContext("2d");
      context.drawImage(this.$refs.camera, 0, 0, 450, 337.5);
    },

    downloadImage() {
      const download = document.getElementById("downloadPhoto");
      const canvas = document
        .getElementById("photoTaken")
        .toDataURL("image/jpeg")
        .replace("image/jpeg", "image/octet-stream");
      download.setAttribute("href", canvas);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
$trans_duration: 0.3s;
body {
  display: flex;
  justify-content: center;
  li {
    list-style: none;
  }
}

.web-camera-container {
  margin-top: 2rem;
  margin-bottom: 2rem;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 500px;

  .camera-button {
    margin-bottom: 2rem;
  }

  .camera-box {
    .camera-shutter {
      opacity: 0;
      width: 450px;
      height: 337.5px;
      background-color: #fff;
      position: absolute;

      &.flash {
        opacity: 1;
      }
    }
  }

  .camera-shoot {
    margin: 1rem 0;

    button {
      height: 60px;
      width: 60px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 100%;

      img {
        height: 35px;
        object-fit: cover;
      }
    }
  }

  .camera-loading {
    overflow: hidden;
    height: 100%;
    position: absolute;
    width: 100%;
    min-height: 150px;
    margin: 3rem 0 0 -1.2rem;

    ul {
      height: 100%;
      position: absolute;
      width: 100%;
      z-index: 999999;
      margin: 0;
    }

    .loader-circle {
      display: block;
      height: 14px;
      margin: 0 auto;
      top: 50%;
      left: 100%;
      transform: translateY(-50%);
      transform: translateX(-50%);
      position: absolute;
      width: 100%;
      padding: 0;

      li {
        display: block;
        float: left;
        width: 10px;
        height: 10px;
        line-height: 10px;
        padding: 0;
        position: relative;
        margin: 0 0 0 4px;
        background: #999;
        animation: preload 1s infinite;
        top: -50%;
        border-radius: 100%;

        &:nth-child(2) {
          animation-delay: 0.2s;
        }

        &:nth-child(3) {
          animation-delay: 0.4s;
        }
      }
    }
  }

  @keyframes preload {
    0% {
      opacity: 1;
    }
    50% {
      opacity: 0.4;
    }
    100% {
      opacity: 1;
    }
  }
}
.questionContainer {
  white-space: normal;

  height: 100%;
  width: 100%;

  .optionContainer {
    margin-top: 12px;
    flex-grow: 1;
    .option {
      border-radius: 290486px;
      padding: 9px 18px;
      margin: 0 18px;
      margin-bottom: 12px;
      transition: $trans_duration;
      cursor: pointer;
      background-color: rgba(0, 0, 0, 0.05);
      color: rgba(0, 0, 0, 0.85);
      border: transparent 1px solid;

      &.is-selected {
        border-color: rgba(black, 0.25);
        background-color: white;
      }
      &:hover {
        background-color: rgba(0, 0, 0, 0.1);
      }
      &:active {
        transform: scaleX(0.9);
      }
    }
  }

  .questionFooter {
    background: rgba(0, 0, 0, 0.025);
    border-top: 1px solid rgba(0, 0, 0, 0.1);
    width: 100%;
    align-self: flex-end;

    .pagination {
      //padding: 10px 15px;
      margin: 15px 25px;
    }
  }
}
</style>
