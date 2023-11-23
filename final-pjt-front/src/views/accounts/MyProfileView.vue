<template>
  <div>
    <h1>사용자 정보</h1>
    <div v-if="isLoading" class="loading">
      로딩 중...
    </div>
    <div v-else-if="userInfo" class="user-info">
      <p><strong>아이디:</strong> {{ userInfo.username }}</p>
      <p><strong>닉네임:</strong> {{ userInfo.nickname }}</p>
    </div>
    <div v-else class="error">
      사용자 정보를 가져오는데 실패했습니다.
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

<style scoped>
.user-info {
  background-color: #f4f4f4;
  padding: 20px;
  border-radius: 5px;
  margin-top: 20px;
}

.loading {
  font-style: italic;
  color: #888;
  margin-top: 20px;
}

.error {
  color: red;
  margin-top: 20px;
}
</style>