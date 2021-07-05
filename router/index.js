import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Kkobuki",
    component: () => import("../src/components/Kkobuki.vue")
  },
  {
    path: "/timer",
    name: "Timer",
    component: () => import("../src/components/Timer.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
