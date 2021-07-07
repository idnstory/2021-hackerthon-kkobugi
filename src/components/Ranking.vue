<template>
  <div id="ranking" class="container">
    <h2>오늘의 랭킹:</h2>
    <p>
    <ul id="example-2">
      <li v-for="(item,index) in infoList" v-bind:key="item.id">
         {{ index }} : {{ item.name }} : {{ item.score }} : {{ item.created }}
      </li>
    </ul>
    </p>
    <b-button
      class="align-self-end"
      variant="outline-info"
      size="lg"
      @click="replay()"
      block
      >Replay</b-button
    >
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Ranking",
  props: {},
  data() {
    return {
      infoList: '',
    };
  },
  methods: {
    // ranking(count, name) {
    //   const nameAndCount = {
    //     name: name,
    //     count: count
    //   };
    //   // nameAndCountArray.push(nameAndCount);
    //   // nameAndCountArray.sort(NumberCompare);
    //   const rankingElem = document.getElementById("ranking");
    //   const printArray = [];
    //   for (var i = 0; i < nameAndCountArray.length; i++) {
    //     if (i >= 5) {
    //       break;
    //     }
    //     printArray.push(
    //       i +
    //         1 +
    //         "등 : " +
    //         nameAndCountArray[i].name +
    //         " " +
    //         nameAndCountArray[i].count +
    //         "회"
    //     );
    //   }
    //   rankingElem.innerHTML = printArray.join("<br/>");
    // },
    NumberCompare(a, b) {
      return a.count - b.count;
    },
    replay() {
          this.$router.push({ path: '/' });
    },
  },
  coumputed: {
    // listDate() {
    //   return this.infoList.created
    // }
  },
  mounted () {
    axios
      //.get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .get('http://kkobuki.haezoom.io:8080/ranking/ranking/')
      .then(response => (this.infoList = response.data))
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
  .container {

  }
  li {
    list-style: none;
    font-size: 20px;
  }
</style>
