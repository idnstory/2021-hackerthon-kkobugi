<template>
  <div id="ranking">
    <h2>랭킹은?</h2>
    <ul id="example-1">
      <li v-for="item in totalLists" v-bind:key="item.id">
        {{ item.rank }}. {{ item.name }} : {{ item.score }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "Ranking",
  props: {},
  data() {
    return {
      totalLists: [
        { rank: "", name: "한승", score: "" },
        { rank: "", name: "지영", score: "" },
        { rank: "", name: "유리", score: "" }
      ]
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
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
