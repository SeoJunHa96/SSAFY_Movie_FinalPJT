import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  // API_URL을 먼저 정의합니다.
  const router = useRouter()
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  // 반응형 객체로 token을 정의합니다.
  const token = ref(null) // 로컬 스토리지에서 토큰 가져오기
  const local = localStorage.getItem('token')
  if(local!==null && local!==undefined) {
    token.value = local
  }
  const isLogin = computed(() => !!token.value) // 수정된 computed

  const saveToken = (tokenValue) => {
    localStorage.setItem('token', tokenValue) // 로컬 스토리지에 토큰 저장
    token.value = tokenValue // 상태 저장소에 토큰 설정
  }

  const clearToken = () => {
    localStorage.removeItem('token') // 로컬 스토리지에서 토큰 삭제
    token.value = null // 상태 저장소에서 토큰 삭제
  }

  const signUp = function (payload) {
    const { username, nickname, password, password2} = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, nickname, password, password2,
      },
    })
      .then((res) => {
        console.log(res)
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logIn = function(payload) {
    const { username, password } = payload
  
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log(res.data)
        saveToken(res.data.token); // 새로운 토큰 저장
        router.push({ name: 'home'})
      })
      .catch((err) => console.log('로그인왜안됨'))
  }
  
  const logOut = function () {
    axios({
      method: 'delete',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        clearToken(); // 로그아웃 시 토큰 삭제
        router.push({ name: 'home' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

const getArticles = function () {
  axios({
    method: 'get',
    url: `${API_URL}/community/article_list_create/`,
  })
    .then((res) =>{
      articles.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
}

const createArticle = function (payload) {
  const { title, content } = payload
  axios({
    method: 'post',
    url: `${API_URL}/community/article/create/`,
    data: {
      title: title,
      content: content
    },
    headers: {
      Authorization: `Token ${token.value}`
    }
  })
    .then((res) => {
      console.log(res)
      router.push({ name: 'CommunityView' })
    })
    .catch((err) => {
      console.log(err)
    })
}

  return { API_URL, articles, API_URL, signUp, logIn, logOut, token, isLogin, getArticles, createArticle, }
}, { persist: true})
