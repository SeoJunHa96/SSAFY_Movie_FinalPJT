<template>
    <div>
      <h1>배우 정보</h1>
      <div v-if="actor" class="actor-container">
        <div class="profile-container">
          <img :src="getProfileUrl(actor.profile_path)" alt="actor_img">
        </div>
        <div class="info-container">
          <p>이름 : {{ actor.name }}</p>
          <p>생일 : {{ actor.birthday }} ({{ actor.place_of_birth }})</p>
          <p v-if="actor.deathday">사망 : {{ actor.deathday }}</p>
          <p>성별 : 
            <span v-if="actor.gender === 1">여</span>
            <span v-else-if="actor.gender === 2">남</span>
          </p>
          <p>소개 : {{ actor.biography }}</p>
        </div>
      </div>
      <hr>
      <h2>필모그래피</h2>
      <div class="movie-cards">
          <MovieList
              v-for="movie in movies"
              :key="movie.id"
              :movie="movie"
              class="movie-card"
          />
      </div>
    </div>
  <hr>
  </template>
    
    <script setup>
    import axios from 'axios'
    import { onMounted, ref } from 'vue'
    import { useRoute } from 'vue-router'
    import MovieList from '@/components/movie/MovieList.vue'
    
    const actor = ref([]);
    const movies = ref([]);
    const loading = ref(true);
    const route = useRoute()
    
    const fetchActorInfo = async () => {
      const apiKey = '3691eda9c0d72053e1652d747c826899';
      const apiUrl = `https://api.themoviedb.org/3/person/${route.params.id}?api_key=${apiKey}&language=en-US`;
    
      try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        actor.value = {
          name: data.name,
          birthday: data.birthday,
          deathday: data.deathday,
          gender: data.gender,
          place_of_birth: data.place_of_birth,
          profile_path: data.profile_path,
          biography: data.biography,
        }
        loading.value = false;
      } catch (error) {
        console.error('데이터 불러오기 오류:', error);
        loading.value = false;
      }
    };
  
    const fetchMovies = async () => {
      const apiKey = '3691eda9c0d72053e1652d747c826899';
      const apiUrl = `https://api.themoviedb.org/3/person/${route.params.id}/movie_credits?api_key=${apiKey}&language=ko-KR`;
    
      try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        movies.value = data.cast.slice(0,7);
        loading.value = false;
      } catch (error) {
        console.error('데이터 불러오기 오류:', error);
        loading.value = false;
      }
    };
  
    const getProfileUrl = (relativePath) => {
      if (relativePath) {
        return `https://image.tmdb.org/t/p/w500${relativePath}`;
      }
      return '';
    };
    
    onMounted(() => {
      fetchActorInfo();
      fetchMovies();
    });
    </script>
    
    <style scoped>
    .actor-container {
      display: flex;
    }
    
    .profile-container {
      margin-right: 20px;  /* 오른쪽으로 여유를 주어 포스터와 정보를 구분 */
    }
    
    .info-container {
      flex: 1;  /* 남은 공간을 모두    차지하도록 설정하여 오른쪽에 텍스트 정보를 정렬 */
    }
  
    .movie-card {
    display: inline-block;
    text-align: center;
    margin: 10px;
    }
    </style>
    