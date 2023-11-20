import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  // API_URL을 먼저 정의합니다.
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  // 반응형 객체로 token을 정의합니다.
  const token = ref(null)

  const signUp = function (payload) {
    const { username, nickname, password1, password2, sign_like_movie, like_genre } = payload
    
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, nickname, password1, password2, sign_like_movie, like_genre,
      }
    })
      .then(res => {
        console.log('회원가입 완료')
      })
      .catch(err => console.log(err))
  }

  const login = function(payload) {
    const username = payload.username
    const password = payload.password

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(res => {
        token.value = res.data.key
      })
      .catch(err => console.log(err))
  }
  
  const getArticles = function() {
    axios({
      method: `get`,
      url: `${API_URL}/community/articles`
    })
      .then(res => {
        articles.value = res.data
      })
      .catch(err => console.log(err))
  }

  return { articles, API_URL, signUp, login, token, getArticles }
}, { persist: true})
