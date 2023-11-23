<template>
  <div class="main-container">
    <h1>영화 정보</h1>
    <hr>
    <div v-if="movie" class="movie-container">
      <div class="poster-container">
        <img :src="getPosterUrl(movie.poster_path)" alt="movie_poster">
      </div>
      <div class="info-container">
        <p class="title">제목 : {{ movie.title }}</p>
        <p class="releasedate">개봉일 : {{ movie.release_date }}</p>
        <p class="popularity">인지도 : {{ movie.popularity }}</p>
        <p class="runtime">상영시간 : <span v-if="Math.floor(movie.runtime/60)">{{ Math.floor(movie.runtime/60) }}시간</span> {{ movie.runtime % 60 }}분</p>
        <p class="genre">장르 : 
        <span v-for="(genre, index) in movie.genres" :key="genre.id">
            {{ genre.name }}<span v-if="index !== movie.genres.length - 1">, </span>
        </span>
        </p>
        <p class="overview">줄거리 : {{ movie.overview }}</p>
      </div>
    </div>
    <h2>출연 배우</h2>
    <hr>
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
    return `https://image.tmdb.org/t/p/w400${relativePath}`;
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
  margin-top: 25px;
  margin-left: 100px;
  margin-right: 100px;
  background-color: rgba(255, 255, 255, 0.7);
  border-radius: 5px;
  width: auto;
}
.main-container > h1,
.main-container > h2 {
  padding-top: 20px;
  margin-left: 50px;
  padding-bottom: 10px;
}
  .movie-container {
    display: flex;
    justify-content: center;
  }
  
  .poster-container {
    margin: 10px;
  }
  
  .info-container {
    /* flex: 1;  남은 공간을 모두    차지하도록 설정하여 오른쪽에 텍스트 정보를 정렬 */
    margin: 30px;
    width: 500px;
  }
  .info-container > .title {
    /* flex: 1;  남은 공간을 모두    차지하도록 설정하여 오른쪽에 텍스트 정보를 정렬 */
    font-weight: bold;
    font-size: 150%;
  }

  .actor-cards {
    display: inline-block;
    text-align: center;
  }
  .actor-card {
    display: inline-block;
    text-align: center;
    width: 220px;
    height: 330px;
    margin: 10px;
  }
</style>
  