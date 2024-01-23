// EventBus
import Vue from "vue";
let bus = new Vue();
Vue.prototype.$EventBus = bus;
export default bus;