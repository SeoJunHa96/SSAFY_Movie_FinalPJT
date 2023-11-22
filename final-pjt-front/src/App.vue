<template>
  <div>
    <div style="display: flex; justify-content: flex-end;">
      <br>
    </div>
    <b-navbar toggleable="lg" type="white" variant="white">
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <div style="display: flex; align-items: center; justify-content: space-between; width: 100%;">
          <b-navbar-nav>
            <router-link to="/profile" class="nav-link">My Profile</router-link>
            <router-link to="/movieview" class="nav-link">Recommend</router-link>
            <router-link to="/movierank" class="nav-link">Movie Ranking</router-link>
            <RouterLink :to="{ name:'CommunityView'}" class="nav-link">Review</RouterLink>
          </b-navbar-nav>
          <router-link to="/" class="logo-link"><img src="@/assets/logo.png" alt="LOGO" style="width: 95px" /></router-link>
          <div><RouterLink :to="{ name: 'LoginView' }">로그인</RouterLink> |
            <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink>|
            <a v-if="isLogin" @click="logOut" class="account-link">로그아웃</a>
          </div> 
        </div>
      </b-collapse>
    </b-navbar>
    <div style="margin-top: 2rem;">
      <hr>
      <RouterView />
    </div>
    <footer class="custom-footer">
      <p>Project By<br />SEO JUN HA & JEONG SE JIN</p> <br />
      <a href="https://github.com/SeoJunHa96/SSAFY_Movie_FinalPJT" class="github-link">https://github.com/SeoJunHa96/SSAFY_Movie_FinalPJT</a>
    </footer>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const isLogin = store.isLogin

const logOut = () => {
    store.logOut()
}

</script>

<style lang="scss">
@import '@/css/common.css';
@import '@/css/reset.css';

/* Add your scoped styles here */
.navbar-custom {
  background-color: rgb(255, 255, 255);
  color: white;
}

/* Navbar links */
.navbar-custom .navbar-nav .nav-link {
  color: white;
  font-weight: bold;
}
.logo-link {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}

.custom-footer {
  bottom: 0;
  width: 100%;
  text-align: center;
  padding: 1rem 0;
  background-color: lightgray;
  font-size: 0.6em;
}

.custom-footer p {
  margin: 0;
}

.github-link {
  color: inherit; 
  text-decoration: none; 
  font-style: italic; 
  display: block; 
}
</style>
