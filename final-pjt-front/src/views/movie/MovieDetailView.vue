<template>
  <div class="main-container">
    <h1>영화 정보</h1>
    <div v-if="movie" class="movie-container">
      <div class="poster-container">
        <img :src="getPosterUrl(movie.poster_path)" alt="movie_poster">
      </div>
      <div class="info-container">
        <p>제목 : {{ movie.title }}</p>
        <p>개봉일 : {{ movie.release_date }}</p>
        <p>인지도 : {{ movie.popularity }}</p>
        <p>상영시간 : {{ movie.runtime }}</p>
        <p>장르 : 
        <span v-for="(genre, index) in movie.genres" :key="genre.id">
            {{ genre.name }}<span v-if="index !== movie.genres.length - 1">, </span>
        </span>
        </p>
        <p>줄거리 : {{ movie.overview }}</p>
      </div>
    </div>
    <hr>
    <h2>출연 배우</h2>
    <div class="actor-cards">
      <ActorList
        v-for="actor in actors"
        :key="actor.id"
        :actor="actor"
        class="actor-card"
      />
    </div>
  </div>
<hr>
</template>
  
<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import ActorList from '@/components/movie/ActorList.vue'

const movie = ref([]);
const actors = ref([]);
const loading = ref(true);
const route = useRoute()
const hoveredMovie = ref(null);

const fetchMovieInfo = async () => {
  const apiKey = '3691eda9c0d72053e1652d747c826899';
  const apiUrl = `https://api.themoviedb.org/3/movie/${route.params.id}?api_key=${apiKey}&language=ko-KR`;

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    movie.value = {
      title: data.title,
      release_date: data.release_date,
      popularity: data.popularity,
      runtime: data.runtime,
      overview: data.overview,
      poster_path: data.poster_path,
      genres: data.genres,
    }
    loading.value = false;
  } catch (error) {
    console.error('데이터 불러오기 오류:', error);
    loading.value = false;
  }
};

const fetchActors = async () => {
  const apiKey = '3691eda9c0d72053e1652d747c826899';
  const apiUrl = `https://api.themoviedb.org/3/movie/${route.params.id}/credits?api_key=${apiKey}&language=ko-KR`;

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    actors.value = data.cast.slice(0,7);
    loading.value = false;
  } catch (error) {
    console.error('데이터 불러오기 오류:', error);
    loading.value = false;
  }
};

const getPosterUrl = (relativePath) => {
  if (relativePath) {
    return `https://image.tmdb.org/t/p/w500${relativePath}`;
  }
  return '';
};

onMounted(() => {
  fetchMovieInfo();
  fetchActors();
});

</script>
  
<style scoped>
.main-container {
  margin-left: 50px;
  margin-right: 50px;
}
  .movie-container {
    display: flex;
  }
  
  .poster-container {
    margin-right: 20px;  /* 오른쪽으로 여유를 주어 포스터와 정보를 구분 */
  }
  
  .info-container {
    flex: 1;  /* 남은 공간을 모두    차지하도록 설정하여 오른쪽에 텍스트 정보를 정렬 */
  }

  .actor-card {
  display: inline-block;
  text-align: center;
  margin: 10px;
  }
</style>
  