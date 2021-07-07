import Vue from "vue";
import LoadScript from "vue-plugin-load-script";
import VueRouter from "vue-router";

Vue.use(VueRouter);
Vue.use(LoadScript);
Vue.loadScript(
  "https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"
);
Vue.loadScript(
  "https://cdn.jsdelivr.net/npm/@teachablemachine/pose@0.8/dist/teachablemachine-pose.min.js"
);

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
