import { createApp, inject, reactive } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'
import router from './router'
import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import store from './store' // Vuex store import
// import '@/css/common.css';
// import '@/css/reset.css';

const app = createApp(App)
const pinia = createPinia()
app.use(pinia)
pinia.use(piniaPluginPersistedstate)

const eventbusSymbol = Symbol()

// eventbus를 reactive 객체로 생성
const eventbus = reactive({
  searchText: '',
  check: '',
  passSearchTxt(searchText, check) {
    this.searchText = searchText;
    this.check = check;
  },
});

// provide로 eventbus를 전역으로 제공
app.provide('eventbus', {
  ...eventbus,
  [eventbusSymbol]: app,
});

app.use(store) // Vuex store 등록
app.use(BootstrapVue3)
app.use(router)
app.mount('#app')
