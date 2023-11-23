<template>
  <div class="main-container">
    <div class="button-container">
      <button @click="showMovieVote" :class="{ active: activeComponent === 'movievote' }" class="btn">평점</button>
      <button @click="showMoviePopular" :class="{ active: activeComponent === 'moviepopular' }" class="btn">인기도</button>
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
  align-items: center;
}

.button-container {
  display: flex;
  justify-content: center;
}

.btn {
  background-color: #ccc;
  color: #000;
  width: 200px; /* 버튼 가로 크기 조정 */
  height: 50px; /* 버튼 세로 크기 조정 */
  border-radius: 10px;
  margin: 10px;
}

.active {
  background-color: #999;
}

</style>