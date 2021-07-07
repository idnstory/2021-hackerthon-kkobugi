<template>
  <div class="base-timer centerp-block">
    <h1 class="font-50">스트레칭방법</h1>
    <ul class="mb-4">
      <li>상반신이 나오도록 카메라에 서주세요</li>
      <li>동작을 5초동안 유지해주세요</li>
    </ul>
    <svg
      class="base-timer__svg"
      viewBox="0 0 100 100"
      xmlns="http://www.w3.org/2000/svg"
    >
      <g class="base-timer__circle">
        <circle
          class="base-timer__path-elapsed"
          cx="50"
          cy="50"
          r="45"
        ></circle>
        <path
          :stroke-dasharray="circleDasharray"
          class="base-timer__path-remaining"
          :class="remainingPathColor"
          d="
            M 50, 50
            m -45, 0
            a 45,45 0 1,0 90,0
            a 45,45 0 1,0 -90,0
          "
        ></path>
      </g>
    </svg>
    <span class="base-timer__label">{{ formattedTimeLeft }}</span>
  </div>
</template>

<script>
const FULL_DASH_ARRAY = 283;
const WARNING_THRESHOLD = 5;
const ALERT_THRESHOLD = 3;
const COLOR_CODES = {
  info: {
    color: "green"
  },
  warning: {
    color: "orange",
    threshold: WARNING_THRESHOLD
  },
  alert: {
    color: "red",
    threshold: ALERT_THRESHOLD
  }
};
const TIME_LIMIT = 5;
export default {
  name: "Timer",
  props: {},
  data() {
    return {
      timeLimit: 5,
      timePassed: 0,
      timerInterval: null
    };
  },
  methods: {
    onTimesUp() {
      clearInterval(this.timerInterval);
    },

    startTimer() {
      this.timerInterval = setInterval(() => (this.timePassed += 1), 1000);
    }
  },
  computed: {
    circleDasharray() {
      return `${(this.timeFraction * FULL_DASH_ARRAY).toFixed(0)} 283`;
    },

    formattedTimeLeft() {
      const timeLeft = this.timeLeft;
      const minutes = Math.floor(timeLeft / 60);
      let seconds = timeLeft % 60;

      if (seconds < 10) {
        seconds = `0${seconds}`;
      }

      return `${minutes}:${seconds}`;
    },

    timeLeft() {
      return TIME_LIMIT - this.timePassed;
    },

    timeFraction() {
      const rawTimeFraction = this.timeLeft / TIME_LIMIT;
      return rawTimeFraction - (1 / TIME_LIMIT) * (1 - rawTimeFraction);
    },

    remainingPathColor() {
      const { alert, warning, info } = COLOR_CODES;

      if (this.timeLeft <= alert.threshold) {
        return alert.color;
      } else if (this.timeLeft <= warning.threshold) {
        return warning.color;
      } else {
        return info.color;
      }
    }
  },
  watch: {
    timeLeft(newValue) {
      if (newValue === 0) {
        this.onTimesUp();
      }
    }
  },
  mounted() {
    this.startTimer();
    setTimeout(() => {
      this.$router.push("/camera1");
    }, 5500);
  }
};
</script>
<style scoped lang="scss">
.font {
  &-20 {
    font-size: 20px;
  }
  &-30 {
    font-size: 20px;
  }
  &-50 {
    font-size: 50px;
  }
}
li {
  list-style: none;
  font-size: 25px;
}
.base-timer {
  position: relative;
  padding-top: 60px;
  margin: 0 auto;
  width: 50%;
  height: 50%;

  &__svg {
    transform: scaleX(-1);
  }

  &__circle {
    fill: none;
    stroke: none;
  }

  &__path-elapsed {
    stroke-width: 7px;
    stroke: #fff;
  }

  &__path-remaining {
    stroke-width: 7px;
    stroke-linecap: round;
    transform: rotate(90deg);
    transform-origin: center;
    transition: 1s linear all;
    fill-rule: nonzero;
    stroke: currentColor;

    &.green {
      color: rgb(65, 184, 131);
    }

    &.orange {
      color: #0dcaf0;
    }

    &.red {
      color: #35a5d7;
    }
  }

  &__label {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 100px;
    font-weight: bold;
  }
}
</style>
