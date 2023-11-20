import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  // API_URL을 먼저 정의합니다.
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()

  // 반응형 객체로 token을 정의합니다.
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const signUp = function (payload) {
    const { username, password1, password2} = payload
    
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2,
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function(payload) {
    const username = payload.username
    const password = payload.password

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        router.push({ name: 'home'})
      })
      .catch((err) => console.log(err))
  }
  
  const logOut = function() {
    // 로그아웃 API 호출
    axios({
        method: 'post',
        url: `${API_URL}/accounts/logout/`,
        // 로그아웃 요청 시 토큰 또는 인증 정보 전달 가능
        headers: {
            Authorization: `Token ${token.value}` // 토큰 또는 인증 정보
        }
    })
    .then(() => {
        // 로그아웃 후 클라이언트 측에서 로컬 스토리지에 저장된 토큰 등 제거
        token.value = null;
        // 다른 클라이언트 정보 제거 (예: 쿠키)
        // ...
        router.push({ name: 'home' }); // 로그인 페이지로 이동
    })
    .catch((err) => console.log(err));
}

const getArticles = function () {
  axios({
    method: 'get',
    url: `${API_URL}/community/articles/`,
    headers: {
      Authorization: `Token ${token.value}`
    }
  })
    .then((res) =>{
      // console.log(res)
      articles.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
}


  return { articles, API_URL, signUp, logIn, logOut, token, isLogin, getArticles }
}, { persist: true})
