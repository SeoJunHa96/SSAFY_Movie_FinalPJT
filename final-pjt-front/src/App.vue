<template>
  <div id="app">
    <div class="background-image"></div>
    <div style="display: flex; justify-content: flex-end;">
      <br>
    </div>
   
        <div style="display: flex; align-items: center; justify-content: space-between; width: 100%;" class="headersection">
          <router-link to="/" class="logo-link">
            <img src="@/assets/logo.png" alt="LOGO" />
          </router-link>
          <nav class="nav-menu">
            <router-link to="/profile" class="nav-link">내 프로필</router-link>
            <router-link to="/movieview" class="nav-link">추천 영화</router-link>
            <router-link to="/movierank" class="nav-link">영화 순위</router-link>
            <RouterLink :to="{ name:'CommunityView'}" class="nav-link">리뷰 게시판</RouterLink>
          </nav>
          <div class="movebutton">
            <template v-if="isLogin">
              <button @click="logOut" class="accountbutton">로그아웃</button>
            </template>
            <template v-else>
              <div class="auth-buttons">
                <RouterLink :to="{ name: 'LoginView' }" class="account-link"><span class="accountbutton">로그인</span></RouterLink>
                <RouterLink :to="{ name: 'SignUpView' }" class="account-link"><span class="accountbutton">회원가입</span></RouterLink>
              </div>
            </template>
          </div>
        </div>
    <div class="router-view-container">
      <hr style="margin: 5px;">
      <RouterView class="routerview"/>
    </div>
    <footer class="custom-footer">
      <p>Project By<br /><strong><a href="https://github.com/SeoJunHa96" style="text-decoration: none;" class="github-link">SEO JUN HA</a> & <a href="https://github.com/LikeBear95" style="text-decoration: none;" class="github-link">JEONG SE JIN</a></strong></p>
      <a href="https://github.com/SeoJunHa96/SSAFY_Movie_FinalPJT" class="github-link">https://github.com/SeoJunHa96/SSAFY_Movie_FinalPJT</a>
    </footer>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore();
const isLogin = store.isLogin;

const logOut = () => {
  store.logOut();
  location.reload(); // 새로고침
};
</script>

<style lang="scss">
/* your existing styles */
.headersection {
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 10px; /* 예시로 패딩값 조정 */
  background: none; /* 배경을 초기화합니다. */
  backdrop-filter: blur(2px); /* 배경에 블러 효과를 추가합니다. */
}

.logo-link {
  display: block;
  
}
.logo-link img {
  width: 260px; /* 원하는 너비값으로 조절해보세요 */
  height: 100px; /* 높이 자동으로 조정되도록 설정 */
  margin: 10px -50px 20px 100px;
}
.nav-menu {
  display: flex; /* 요소들을 수평으로 배치하기 위해 flex로 설정합니다. */
  gap: 50px; /* 요소들 사이의 간격을 조절합니다. */
}
.nav-menu .nav-link {
  display: flex;
  align-items: center;
  margin: 0px 20px; /* 네비게이션 메뉴 간격 조정 */
  font-size: 28px;
  color: #282828;
  text-decoration: none;
  position: relative;
  padding: 6px 12px;
  
}

.nav-menu .nav-link::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 0%;
  height: 4px;
  background: #0000FF;
  transition: all .3s ease-out;
}

.nav-menu .nav-link:hover::after {
  width: 100%;
}

.account-link {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: black;
  color: white;
  text-decoration: none;
  border: none;
  border-radius: 40px;
  height: 70px;
  width: 120px;
  position: relative;
  transition: background-color 0.3s;
}

.accountbutton {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: black;
  color: white;
  text-decoration: none;
  border: none;
  border-radius: 40px;
  height: 70px;
  width: 120px;
  position: relative;
  transition: background-color 0.3s;
}

.account-link:hover {
  background-color: #333;
  color: #00ff0d;
  cursor: pointer;
}
.auth-buttons {
  display: flex;
  gap: 30px;
}
.accountbutton:hover {
  background-color: #333;
  color: #00ff0d;
  cursor: pointer;
}

#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* 최소 높이를 브라우저 높이만큼 지정 */
}

.custom-footer {
  margin-top: auto; /* 페이지가 넘칠 때 푸터가 항상 아래에 위치하도록 함 */
  background-color: #333;
  color: white;
  text-align: center;
  padding: 15px;
  width: 100%;
}
.github-link {
  color: #fff;
  text-decoration: none;
}
.github-link:hover {
  color: rgb(127, 127, 216); 
}
.router-view-container {
  min-height: calc(100vh - 200px);
  overflow-y: auto; 
}
.background-image {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-image: url('@/assets/login.png/');
  background-size: cover;
  opacity: 0.5; /* 배경 이미지 투명도 조절 */
  z-index: -1; /* 배경 이미지가 가장 뒤에 표시되도록 z-index 설정 */
}
.hiddenclass {
  background: none;
}
.movebutton {
  margin: 0px 100px 0px 0px;;
}
</style>
