<template>
    <div class="search-bar">
      <input type="text" v-model="searchTerm" placeholder="영화 제목, 배우, 감독 등으로 검색하세요." />
      <button type="submit" @click="search">검색</button>
    </div>
    <div class="search-results">
      <ul>
        <li v-for="movie in searchResults" :key="movie.id">
          <a :href="`/movies/${movie.id}`">
            <img :src="getImageUrl(movie.poster_path)" alt="Movie Poster" />
            <span>{{ movie.title }}</span>
          </a>
        </li>
      </ul>
    </div>
  </template>

<script setup>
import { ref } from 'vue';
import { getImageUrl } from '@/utils';

const searchTerm = ref('');
const searchResults = ref([]);

const apiKey = '3691eda9c0d72053e1652d747c826899'
const search = () => {
  // 검색어를 API에 전달하여 검색 결과를 가져옵니다.
  const apiUrl = `https://api.themoviedb.org/3/search/movie?api_key=${apiKey}&language=ko-KR&query=${searchTerm.value}`;
  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      searchResults.value = data.results;
    });
};
</script>

<style scoped>
.search-bar {
  position: relative;
  width: 100%;
  height: 50px;
  background-color: #fff;
  border-bottom: 1px solid #ddd;
}

.search-bar input {
  width: 100%;
  height: 40px;
  padding: 10px;
  border: none;
  outline: none;
}

.search-bar button {
  position: absolute;
  right: 10px;
  top: 10px;
  width: 40px;
  height: 40px;
  background-color: #000;
  color: #fff;
  border: none;
  outline: none;
  cursor: pointer;
}

.search-results {
  margin-top: 20px;
}

.search-results ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.search-results li {
  margin-bottom: 10px;
}

.search-results li a {
  display: block;
  width: 100%;
  height: 100px;
}

.search-results li a img {
  width: 100%;
  height: 100%;
}
</style>