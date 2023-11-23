<template>
  <div>
    <div style="display: flex; justify-content: flex-end;">
      <br>
    </div>
    <b-navbar toggleable="lg" type="white" variant="white">
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <div style="display: flex; align-items: center; justify-content: space-between; width: 100%;" class="headersection">
          <router-link to="/" class="logo-link">
            <img src="@/assets/logo.png" alt="LOGO" style="width: 95px" />
          </router-link>
          <b-navbar-nav class="nav-menu">
            <router-link to="/profile" class="nav-link">My Profile</router-link>
            <router-link to="/movieview" class="nav-link">Recommend</router-link>
            <router-link to="/movierank" class="nav-link">Movie Ranking</router-link>
            <RouterLink :to="{ name:'CommunityView'}" class="nav-link">Review</RouterLink>
          </b-navbar-nav>
          <div>
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
      </b-collapse>
    </b-navbar>
    <div>
      <hr style="margin: 10px;">
      <RouterView />
    </div>
    <footer class="custom-footer">
      <p>Project By<br />SEO JUN HA & JEONG SE JIN</p>
      <br />
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

<style scoped>
/* your existing styles */
.headersection {
  height: 100px;
  background: #fff;
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 10px; /* 예시로 패딩값 조정 */
}

.logo-link {
  display: block;
}
.nav-menu {
  gap: 100px;
}
.nav-menu .nav-link {
  display: flex;
  align-items: center;
  margin: 0px 20px; /* 네비게이션 메뉴 간격 조정 */
  font-size: 25px;
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
  gap: 10px;
}
.accountbutton:hover {
  background-color: #333;
  color: #00ff0d;
  cursor: pointer;
}
</style>
