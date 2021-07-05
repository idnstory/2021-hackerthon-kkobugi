<template>
  <div id="ranking">
    랭킹
  </div>
</template>

<script>
export default {
  name: "Ranking",
  props: {},
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
