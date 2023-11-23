<template>
  <div v-if="isLoading" class="loading">
    로딩 중...
  </div>
  <div v-else-if="userInfo" class="main-container">
    <div class="user-info">
      <h1>My Profile</h1>
      <hr>
      <div class="user">
        <div class="profile">
          <img src="@/assets/DDAT.jpg" alt="유저 이미지">
          <button>이미지 바꾸기</button>
        </div>
        <div class="info">
          <p><strong>닉네임:</strong> {{ userInfo.nickname }}</p>
          <p><strong>팔로워 / 팔로잉:</strong> 123 / 456</p>
          <p><strong>내가 준 평균 평점:</strong> 4.3 </p>
        </div>
      </div>
    </div>
    <div class="user-movie">
      <h1>{{ userInfo.nickname }}님의 BEST 5</h1>
      <hr>
      <div class="movie">
        <img src="@/assets/poster1.jpg" alt="영화포스터1">
        <img src="@/assets/poster2.jpg" alt="영화포스터2">
        <img src="@/assets/poster3.jpg" alt="영화포스터3">
        <img src="@/assets/poster4.jpg" alt="영화포스터4">
        <img src="@/assets/poster5.jpg" alt="영화포스터5">
      </div>
    </div>
    <div class="user-article">
      <div class="article">
        <h3>{{ userInfo.nickname }} 님이 작성한 게시글</h3>
        <br><br><br><br>
      </div>
      <br>
      <div class="review">
        <h3>{{ userInfo.nickname }} 님이 남긴 한줄평</h3>
        <br><br><br><br>
      </div>
      <br>
      <div class="comment">
        <h3>{{ userInfo.nickname }} 의 댓글</h3>
        <br><br><br><br>
      </div>
    </div>
  </div>
  <div v-else class="error">
    <h1>사용자 정보를 가져오는데 실패했습니다.</h1>
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
@font-face {
  font-family: 'maple';
  src: url('@/assets/MaplestoryBold.ttf');
}
.main-container {
  margin-left: 100px;
  margin-right: 100px;
  font-family: 'maple';
}
.user-info {
  background-color: rgba(255, 255, 255, 0.7);
  padding: 20px;
  border-radius: 5px;
  margin: 20px auto;
  width: 1000px;
}
.user-info > h1 {
  margin-bottom: 1rem;
  margin-left: 50px;
}
.user-info > .user {
  display: flex;
  /* justify-content: center; */
  align-items: center;
}
.user-info > .user > .profile {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-left: 5%;
  margin-bottom: 1rem;
}
.user-info > .user > .profile > img {
  width: 200px;
  height: 200px;
  object-fit: cover;
  border-radius: 50%;
  margin-bottom: 10px;
  background-color: blue;
}
.user-info > .user > .info {
  text-align: left;
  justify-content: center;
  margin-left: 50px;
}
.user-info > .user > .info > p {
  font-size: 200%;
  margin-bottom: 1rem
}
.user-article {
  background-color: rgba(255, 255, 255, 0.7);
  padding: 20px;
  border-radius: 5px;
  margin: 20px auto;
  width: 1000px;
}
.user-article > h1 {
  margin-bottom: 1rem;
  margin-left: 50px;
}
.user-article > .article,
.user-article > .review,
.user-article > .comment {
  margin: 50px;
}
.user-movie {
  background-color: rgba(255, 255, 255, 0.7);
  padding: 20px;
  border-radius: 5px;
  margin: 20px auto;
  width: 1000px;
}
.user-movie > h1 {
  margin-bottom: 1rem;
  text-align: center;
}
.user-movie > .movie {
  display: flex;
  /* flex-direction: column; */
  align-items: center;
  margin-left: 5%;
  margin-bottom: 1rem;
}
.user-movie > .movie > img {
  width: 150px;
  height: 225px;
  /* object-fit: cover; */
  margin: 10px;
  background-color: blue;
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