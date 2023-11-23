<template>
    <div class="movieConts">
      <br><br>
      <h2>장르가 유사한 영화</h2>  
      <div class="movieNumBox">
        <p>( 오른쪽으로 스크롤 하면 순서대로 모든 영화 목록을 볼 수 있습니다. )</p>
      </div>
  
      <div class="dataBox clear">
        <div class="movies clear" v-if="movieResult">
          <div
            class="movieBox"
            v-for="(movie, index) in movieResult"
            :key="index"
          >
            <div class="imgTitle" @click="moveInform(keyWord(movie.keywords), textEdit(movie.title), textEdit(movie.directors.director[0].directorNm), movie.movieSeq)">
              <img :src="posterURL(movie.posters)" :alt="textEdit(movie.title)" />
  
              <div class="hoverBox">
                <p class="director">감독: {{ textEdit(movie.directors.director[0].directorNm) }}</p>
                <p class="story" v-if="movie.plots.plot[0].plotText !== ''">줄거리: {{ movie.plots.plot[0].plotText }}</p>
              </div>
            </div>
  
            <p class="title">
              <span>{{ textEdit(movie.title) }}</span>
              <span class="year">( {{ movie.prodYear }} )</span>
            </p>
          </div>
        </div>
  
        <p class="nodataTxt" v-else>해당하는 영화가 없습니다.</p>
      </div>
  
      <br /><br />
      <button class="gomainBtn" @click.prevent="goMain">
        <span class="arrow">← </span>
        <span class="text"> 검색 페이지로</span>
      </button>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router';
  import { saveInform, saveFirstKey } from '@/utils/cookies.js';
  import store from '@/store/index.js'
  
  
  const router = useRouter();
  
  const inputText = store.state.searchTxtBox.searchTxt;
  const moviedata = store.state.moviedata;
  const movieResult = store.state.result;
  
  const inputTextEdit = (text) => {
    return text.substring(text.indexOf('=') + 1, text.length);
  };
  
  const movieNum = (num) => {
    if (num <= 100) return num;
    else if (num > 100) return 100;
  };
  
  const posterURL = (url) => {
    if (url === '') {
      return 'http://placehold.it/213x303';
    } else if (url.indexOf('|') === -1) {
      return url;
    } else if (url.indexOf('|')) {
      return url.substring(0, url.indexOf('|'));
    }
  };
  
  const textEdit = (text) => {
    return text.replace(/!HE|!HS/g, '');
  };
  
  const goMain = () => {
    router.push('/movieview');
  };
  
  const keyWord = (key) => {
    if (key === '') return;
    else if (key.indexOf(',') === -1) {
      return key;
    } else if (key.indexOf(',')) {
      return key.split(',')[0];
    }
  };
  
  const moveInform = (keyword, movieID, director, movieSeq) => {
    saveInform(`title=${movieID}&director=${director}&movieSeq=${movieSeq}`);
    const searchTxtBox = {
      searchTxt: `title=${movieID}&director=${director}&movieSeq=${movieSeq}`,
    };
    store.commit('MOVIE_ID', searchTxtBox);
    saveFirstKey(`keyword=${keyword}`);
    const keywordFirstBox = {
      searchTxt: `keyword=${keyword}`,
      check: 'keyword',
    };
    store.commit('SIMILAR_MOVIE_API', keywordFirstBox);
    router.push('/inform');
  };
  </script>
  
  <style scoped>
  @import '@/css/common.css';
@import '@/css/reset.css';
  </style>
  