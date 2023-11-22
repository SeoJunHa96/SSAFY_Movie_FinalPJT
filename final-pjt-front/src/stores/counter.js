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
    const { username, nickname, password1, password2} = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, nickname, password1, password2,
      },
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
  
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

const getArticles = function () {
  axios({
    method: 'get',
    url: `${API_URL}/community/article_list_create/`,
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
