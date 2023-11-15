import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const signUp = function (payload) {
    const { username, nickname, password1, password2, sign_like_movie, like_genre } = payload
    const token = ref(null)
    
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


  return { signUp, login, token }
}, { persist: true})
