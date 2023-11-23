<template>
  <div class="main-container">
    <div class="btn">
      <button @click="showMovieVote" :class="{ active: activeComponent === 'movievote' }" class="switch">평점</button>
      <button @click="showMoviePopular" :class="{ active: activeComponent === 'moviepopular' }" class="switch">인기도</button>
    </div>

    <div v-if="activeComponent === 'movievote'">
      <MovieVote />
    </div>

    <div v-else-if="activeComponent === 'moviepopular'">
      <MoviePopular />
    </div>
  </div>
</template>
  
<script setup>
  import { ref } from 'vue';
  import MoviePopular from '@/components/movie/MoviePopular.vue'
  import MovieVote from '@/components/movie/MovieVote.vue'

  const activeComponent = ref('movievote');
  
  const showMovieVote = () => {
    activeComponent.value = 'movievote';
  };
  
  const showMoviePopular = () => {
    activeComponent.value = 'moviepopular';
  };
</script>

<style>
  .main-container {
  margin-left: 50px;
  margin-right: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

  .switch {
    background-color: rgba(128, 128, 128, 0.3);
    color: #000;
    padding: 10px;
    border-radius: 5px;
    margin: 10px;
  }
  
  .active {
    background-color: orange;
    color: white;
    font-weight: bold;
  }
</style>
  