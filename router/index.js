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
  },
  {
    path: "/camera",
    name: "Camera",
    component: () => import("../src/components/Camera.vue")
  },
  {
    path: "/camera1",
    name: "Camera1",
    component: () => import("../src/components/Camera1.vue")
  },
  {
    path: "/ranking",
    name: "Ranking",
    component: () => import("../src/components/Ranking.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
