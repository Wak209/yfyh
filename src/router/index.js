
import { options } from "less";
import { createRouter, createWebHashHistory } from "vue-router";
const routes = [
  {
    path: "/",
    name: "main",
    component: () => import("../pages/Home.vue"),
  },
  {
    path: "/two",
    name: "two",
    component: () => import("../pages/2D.vue"),
  },
  {
    path: "/three",
    name: "three",
    component: () => import("../pages/3D.vue"),
  },
  {
    path: "/others",
    name: "others",
    component: () => import("../pages/others.vue"),
  },
  
];


const  scrollBehavior = (to, from, savedPosition) => {
  if (savedPosition && to.meta.keepAlive) {
    return savedPosition;
  }
  return { x: 0, y:0 };
}


export default createRouter({
  history: createWebHashHistory(),
  routes: routes,
  scrollBehavior,
});

