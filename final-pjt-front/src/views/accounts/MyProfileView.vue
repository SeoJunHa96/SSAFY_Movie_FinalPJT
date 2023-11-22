<template>
  <div v-if="user !== undefined" class="container" style="padding-top: 48px; padding-left: 48px;">
    <h1 class="title-font fw-bold" style="margin-bottom: 30px">
      <span style="font-size: 5rem;">{{ user.nickname }}</span> 님의 프로필
    </h1>
    
    <!-- ... (기타 코드) -->
  </div>
  <div v-else>
    이 페이지인가
    프로필 정보를 불러오는 중입니다...
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useRoute, useRouter } from 'vue-router'

const API_URL = "http://127.0.0.1:8000"

const user = ref(undefined)
const route = useRoute()
const router = useRouter()

console.log('출랴ㅕ')
const getMyProfile = async () => {
  try {
    const token = localStorage.getItem('token')
    if (!token) {
      // 토큰이 없는 경우 처리 (예: 로그인 페이지로 리다이렉트)
      router.push('/login')
      return
    }

    const response = await axios.get(`${API_URL}/profile/`, {
      headers: {
        Authorization: `Token ${token}`
      }
    })

    user.value = response.data
    console.log('사용자 프로필 정보:', response.data)
  } catch (error) {
    console.error('사용자 프로필 요청 중 오류 발생:', error)
    // 에러 처리 (예: 오류 메시지 출력 등)
  }
}

onMounted(() => {
  getMyProfile()
})
</script>

<style scoped>
/* 필요한 스타일이 있다면 추가하세요. */
</style>
