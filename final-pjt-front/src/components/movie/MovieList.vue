<script setup>
import router from '@/router'
defineProps({
    movie: Object
})

const getPosterUrl = (relativePath) => {
    if (relativePath) {
      return `https://image.tmdb.org/t/p/w200${relativePath}`;
    }
    return '';
  };

const goMovie = (movie) => {
    router.push(`/movies/${movie.id}`);
  };
</script>

<template>
    <div v-if="movie" @click="goMovie(movie)">
        <img :src="getPosterUrl(movie.poster_path)" alt="movie_img">
        <p>{{ movie.title }}</p>
    </div>
    <div v-else>로딩중</div>
</template>

<style scoped>

</style>
