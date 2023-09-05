
import { options } from "less";
import { createRouter, createWebHashHistory } from "vue-router";
const routes = [
  {
    path: "/",
    name: "login",
    component: () => import("../pages/login.vue"),
  },
  {
    path: "/before",
    name: "before",
    component: () => import("../pages/before.vue"),
  },
  {
    path: "/after",
    name: "after",
    component: () => import("../pages/after.vue"),
  },
  {
    path: "/pragh",
    name: "pragh",
    component: () => import("../pages/pragh.vue"),
  },
  {
    path: "/user",
    name: "user",
    component: () => import("../pages/user.vue"),
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

