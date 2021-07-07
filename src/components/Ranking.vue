<template>
  <div id="ranking" class="container my-4">
    <h2 class="font-50">오늘의 랭킹</h2>
    <b-table striped hover :items="infoList"></b-table>
    <!-- <ul id="example-2">
      <li v-for="(item, index) in infoList" v-bind:key="item.id">
        {{ index }} : {{ item.name }} : {{ item.score }} : {{ item.created }}
      </li>
    </ul> -->
    <b-button
      class="align-self-end"
      variant="outline-info"
      size="lg"
      @click="replay()"
      block
      >Replay</b-button
    >
    <audio autoplay>
      <source src="../assets/complete2.mp3" type="audio/mp3" />
    </audio>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Ranking",
  props: {},
  data() {
    return {
      infoList: ""
    };
  },
  methods: {
    NumberCompare(a, b) {
      return a.count - b.count;
    },
    replay() {
      this.$router.push({ path: "/" });
    }
  },
  coumputed: {
    // listDate() {
    //   return this.infoList.created
    // }
  },
  mounted() {
    axios
      //.get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .get("http://kkobuki.haezoom.io:8080/ranking/ranking/")
      .then(response => (this.infoList = response.data));
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
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
tbody {
  font-size: 20px;
}
li {
  list-style: none;
  font-size: 20px;
}
</style>
