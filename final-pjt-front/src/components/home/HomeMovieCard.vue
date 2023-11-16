<template>
    <div class="movie-card">
      <img :src="movie.posterUrl" alt="Movie Poster" />
      <div class="movie-info" v-if="isHovered">
        <h2>{{ movie.title }}</h2>
        <p>{{ movie.director }}</p>
        <p>{{ movie.actor }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      movie: {
        type: Object,
        required: true,
      },
    },
    data() {
      return {
        isHovered: false,
      };
    },
    mounted() {
      this.$refs.movieCard.addEventListener("mouseover", () => {
        this.isHovered = true;
        this.movieCard.classList.add("flipped");
      });
      this.$refs.movieCard.addEventListener("mouseleave", () => {
        this.isHovered = false;
        this.movieCard.classList.remove("flipped");
      });
    },
  };
  </script>