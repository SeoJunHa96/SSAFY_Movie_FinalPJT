import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import BootstrapVue3 from 'bootstrap-vue-3'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

const app = createApp(App)
const pinia = createPinia()

// Pinia를 설치한 후 플러그인을 사용해야 합니다.
app.use(pinia)

// 플러그인을 Pinia에 등록합니다.
pinia.use(piniaPluginPersistedstate)

app.use(BootstrapVue3)
app.use(router)

app.mount('#app')
