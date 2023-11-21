<template>
    <div @mouseenter="toggleCard(movie.id)" @mouseleave="toggleCard(null)" @click="goDetail(movie)">
      <img :src="getImageUrl(movie.poster_path)" alt="Movie Poster" class="movie-poster" />
      <div class="movie-info" v-if="hoveredMovie === movie.id">
        <h3>{{ movie.title }}</h3>
        <p>개봉 : {{ movie.release_date }}</p>
        <p>평점 : {{ movie.vote_average }}</p>
        <p>줄거리: {{ movie.overview }}</p>
      </div>
    </div>
</template>

  <script setup>
  import { defineProps } from 'vue'
  import router from '@/router'

  defineProps({
    movie: Object
})

const getImageUrl = (relativePath) => {
    if (relativePath) {
      return `https://image.tmdb.org/t/p/w500${relativePath}`;
    }
    return '';
  };


const goDetail = (movie) => {
    router.push(`/movies/${movie.id}`);
  };
  </script>

  <style>
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