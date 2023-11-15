<template>
    <div>
        <div style="display: flex; justify-content: flex-end;">
          <RouterLink :to="{ name: 'LoginView' }">로그인</RouterLink>
        </div>
        <b-navbar toggleable="lg" type="white" variant="white">
          <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
          <b-collapse id="nav-collapse" is-nav>
            <router-link to="/" class="logo-link"><img src="@/assets/logo.png" alt="LOGO" style="width: 40px" /></router-link>
            <b-navbar-nav class="mx-auto">
              <router-link to="/profile" class="nav-link">My Profile</router-link>
              <router-link to="/movies" class="nav-link">Recommend</router-link>
              <router-link to="/movieranking" class="nav-link">Ranking</router-link>
              <router-link to="/reviews" class="nav-link">Review</router-link>
              <router-link to="/play" class="nav-link">Play</router-link>
            </b-navbar-nav>
          </b-collapse>
        </b-navbar>
      <div style="margin-top: 3rem;"> <!-- 상단 여백 -->
        <router-view></router-view> <!-- 페이지 내용 -->
      </div>
      <footer style="position: fixed; bottom: 0; width: 100%; height: 3rem; background-color: lightgray;">footer</footer> <!-- 푸터 -->
    </div>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router';
  </script>
  
  <style scoped>
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
  </style>
  