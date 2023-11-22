<template>
  <div v-if="movie" class="movie-card" @mouseenter="toggleCard(movie.id)" @mouseleave="toggleCard(null)" @click="goMovie(movie)">
    <img :src="getPosterUrl(movie.poster_path)" alt="movie_img" class="movie-poster">
    <div class="movie-info" v-if="hoveredMovie === movie.id">
      <h3>{{ movie.title }}</h3>
      <p>개봉 : {{ movie.release_date }}</p>
      <p v-if="movie.vote_average == 0">평점 : 집계중</p>
      <p v-else>평점 : {{ movie.vote_average }}</p>
      <p v-if="movie.overview">줄거리: {{ movie.overview }}</p>
      <p v-else>줄거리: 준비중</p>
    </div>
  </div>
  <div v-else>로딩중</div>
</template>

<script setup>
import { ref, defineProps } from 'vue'
import router from '@/router'

defineProps({
    movie: Object
})

const hoveredMovie = ref(null);

const getPosterUrl = (relativePath) => {
  if (relativePath) {
    return `https://image.tmdb.org/t/p/w500${relativePath}`;
  }
  return '';
};

const toggleCard = (id) => {
  hoveredMovie.value = id;
};

const goMovie = (movie) => {
  router.push(`/movies/${movie.id}`);
};
</script>

<style>
.movie-card {
  position: relative;
  border: 1px solid #ddd;
  padding: 10px;
  text-align: center;
}

.movie-poster {
  max-width: 200px; /* 포스터 최대 너비 */
  height: auto;
  display: block;
  margin: 0 auto; /* 가운데 정렬 */
}

.movie-poster {
  max-width: 200px; /* 포스터 최대 너비 */
  height: auto;
  display: block;
  margin: 0 auto; /* 가운데 정렬 */
}
.movie-info {
  display: none;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 10px;
}

.movie-card:hover .movie-info {
  display: block;
}
</style>