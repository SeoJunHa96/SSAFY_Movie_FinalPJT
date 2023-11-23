<template>
    <div class="main-container">
      <h1>배우 정보</h1>
      <hr>
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
      <h2>필모그래피</h2>
      <hr>
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
        return `https://image.tmdb.org/t/p/w400${relativePath}`;
      }
      return '';
    };
    
    onMounted(() => {
      fetchActorInfo();
      fetchMovies();
    });
    </script>
    
    <style scoped>
    .main-container {
  margin-top: 25px;
  margin-left: 50px;
  margin-right: 50px;
  background-color: rgba(255, 255, 255, 0.7);
  border-radius: 5px;
}
.main-container > h1,
.main-container > h2 {
  padding-top: 20px;
  margin-left: 20px;
  padding-bottom: 10px;
}
  .actor-container {
    display: flex;
    justify-content: center;
  }
  
  .profile-container {
    margin-top: 5px;
    margin-left: 5px;
    margin-right: 5px;
  }
  
  .info-container {
    width: 500px;
    margin-top: 15px;
    margin-left: 5px;
    margin-right: 5px;
  }
  
    .movie-cards {
    display: flex;
    text-align: center;
    }
    .movie-card {
    display: inline-block;
    text-align: center;
    width: 250px;
    height: 350px;
    margin: auto 10px;
    }
    </style>
    