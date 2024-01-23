import Vue from 'vue'
import VueRouter from 'vue-router'

import ChartView1 from "@/components/ChartView1";
import ChartView2 from "@/components/ChartView2";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: ChartView1
  },
  {
    path: '/chart1',
    name: 'about',
    component: ChartView1
  },
  {
    path: '/chart2',
    name: 'about',
    component: ChartView2
  }
]

const router = new VueRouter({
  routes
})

export default router
