<template>
  <div>
    <h1>사용자 정보</h1>
    <p v-if="isLoading">로딩 중...</p>
    <div v-else-if="userInfo">
      <p>아이디: {{ userInfo.username }}</p>
      <p>닉네임: {{ userInfo.nickname }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const isLoading = ref(false)
const userInfo = ref(null)
const API_URL = 'http://127.0.0.1:8000'

  // 반응형 객체로 token을 정의합니다.
  const token = ref(null) // 로컬 스토리지에서 토큰 가져오기
  const local = localStorage.getItem('token')
  if(local!==null && local!==undefined) {
    token.value = local
    console.log(token)
  }

  const getUserInfo = async () => {
  isLoading.value = true
  try {
    const res = await axios({
      method: 'get',
      url: `${API_URL}/accounts/profile/`,
      headers: {
        'Authorization': `Token ${token.value}`,
      },
    })
    userInfo.value = res.data
  } catch (err) {
    console.error('사용자 정보를 가져오는데 실패했습니다', err)
  } finally {
    isLoading.value = false
  }
}

onMounted(getUserInfo)
</script>