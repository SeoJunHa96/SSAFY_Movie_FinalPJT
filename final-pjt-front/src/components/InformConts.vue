<template>
    <div class="infromConts" v-if="clickMovieData.Data">
      <div class="topData clear">
        <img
          class="poster"
          :src="posterURL(clickMovieData.Data[0].Result[0].posters)"
          :alt="textEdit(clickMovieData.Data[0].Result[0].title)"
        />
        <div class="summaryBox">
          <div class="title">
            <h2>{{ textEdit(clickMovieData.Data[0].Result[0].title) }} ( {{ clickMovieData.Data[0].Result[0].prodYear }} )</h2>
            <p class="engTitle">{{ clickMovieData.Data[0].Result[0].titleEng }}</p>
          </div>
          <div class="textBox">
            <div class="textList">
              <span>{{ clickMovieData.Data[0].Result[0].genre }}</span>
              <span>{{ clickMovieData.Data[0].Result[0].nation }}</span>
            </div>
            <div class="textList">
              <span>{{ `${dateEdit(clickMovieData.Data[0].Result[0].repRlsDate)} 개봉` }}</span>
              <span>{{ clickMovieData.Data[0].Result[0].runtime }}분</span>
              <span>{{ clickMovieData.Data[0].Result[0].rating }}</span>
            </div>
            <p v-if="clickMovieData.Data[0].Result[0].directors.director[0].directorNm !== ''">(감독) {{ textEdit(clickMovieData.Data[0].Result[0].directors.director[0].directorNm) }}</p>
            <a :href="clickMovieData.Data[0].Result[0].kmdbUrl" target="_blank">영화 상세정보</a>
          </div>
        </div>
      </div>
  
      <div class="detailBox">
        <p class="movieSlogan" v-if="clickMovieData.Data[0].Result[0].plots.plot[0].plotText !== ''">
          {{ sloganEdit(clickMovieData.Data[0].Result[0].plots.plot[0].plotText) }}
        </p>
        <p class="movieStory" v-if="clickMovieData.Data[0].Result[0].plots.plot[0].plotText !== ''">
          {{ storyEdit(clickMovieData.Data[0].Result[0].plots.plot[0].plotText) }}
        </p>
  
        <div class="movieKeyword" v-if="clickMovieData.Data[0].Result[0].keywords">
          <form @click="btnSearch('keywordCK')">
            <button
              v-for="(keyword, keywordIndex) in keywordNum(clickMovieData.Data[0].Result[0].keywords)"
              :key="keywordIndex"
              @click="searchText = keyWord(clickMovieData.Data[0].Result[0].keywords, keywordIndex)"
            >
              {{ `# ${keyWord(clickMovieData.Data[0].Result[0].keywords, keywordIndex)}` }}
            </button>
          </form>
        </div>
  
        <div class="movieStlls" v-if="clickMovieData.Data[0].Result[0].stlls">
          <p>{{ `${photoIndex(clickMovieData.Data[0].Result[0].stlls)}장의 스틸컷` }}</p>
          <div v-for="(photo, imgIndex) in photoIndex(clickMovieData.Data[0].Result[0].stlls)" :key="imgIndex">
            <img :src="stllImgURL(clickMovieData.Data[0].Result[0].stlls, imgIndex)" alt="" />
          </div>
        </div>
  
        <div class="movieActor clear" v-if="clickMovieData.Data[0].Result[0].actors.actor[0].actorNm">
          <p>출연 / 스탭</p>
          <div
            class="actorsBox"
            v-for="(actorName, index) in actorNum(clickMovieData.Data[0].Result[0].actors.actor, actors)"
            :key="index"
          >
            <span class="krNm">{{ actorEdit(actorName.actorNm) }} </span>
            <br />
            <span class="enNm">{{ actorEdit(actorName.actorEnNm) }}</span>
          </div>
          <button v-if="clickMovieData.Data[0].Result[0].actors.actor.length > 10" @click="actorMore(clickMovieData.Data[0].Result[0].actors.actor.length, 'yes')">{{ actorsBtnText }}</button>
        </div>
      </div>
  
      <br />
    </div>
  </template>
  
  <script setup>
  import { saveValue, saveType, deleteCookie, saveFirstKey, getIDFromCookie } from '../utils/cookies';
  import { computed, onMounted, ref } from 'vue';
  import store from '@/store/index.js'

  const imgIndex = ref(0);
  const keywordIndex = ref(0);
  let searchText = ref('');
  let key = ref('');
  let actors = ref(10);
  let actorsAllCheck = ref('no');
  let actorsBtnText = ref('더보기');
  
  const clickMovieData = computed(() => store.state.moviedata);
  
  onMounted(() => {
    const idAPI = store.state.movieID;
    store.dispatch('FETCH_TITLE', idAPI);
    let getMovieID = getIDFromCookie();
  });
  
  const textEdit = (text) => text.replace(/!HE|!HS/g, '');
  const posterURL = (url) => url === '' ? 'http://placehold.it/213x303' : url.indexOf('|') === -1 ? url : url.substring(0, url.indexOf('|'));
  const dateEdit = (date) => date.replace(/(\d{4})(\d{2})(\d{2})/, '$1.$2.$3');
  const sloganEdit = (story) => story.substring(0, story.indexOf('!') + 1);
  const storyEdit = (story) => story.substring(story.indexOf('!') + 1, story.length);
  const keywordNum = (key) => key === '' ? keywordIndex.value = 0 : key.indexOf(',') === -1 ? keywordIndex.value = 1 : keywordIndex.value = key.match(/,/g).length + 1;
  const keyWord = (key, index) => key === '' ? null : key.indexOf(',') === -1 ? key : key.split(',')[index];
  const photoIndex = (photoUrl) => photoUrl === '' ? imgIndex.value = 0 : photoUrl.indexOf('|') === -1 ? imgIndex.value = 1 : imgIndex.value = photoUrl.match(/http/g).length;
  const stllImgURL = (url, index) => url === '' ? 'http://placehold.it/144x86' : url.indexOf('|') === -1 ? url : url.split('|')[index];
  const actorNum = (actors, num) => actors.slice(0, num);
  const actorMore = (all, moreCheck) => {
    if (actorsAllCheck.value === 'no') {
      actors.value = all;
      actorsAllCheck.value = moreCheck;
      actorsBtnText.value = '접기';
    } else if (actorsAllCheck.value === 'yes') {
      actors.value = 10;
      actorsAllCheck.value = 'no';
      actorsBtnText.value = '더보기';
    }
  };
  const actorEdit = (name) => name.match(/!HE | !HS/gi) ? name.replace(/!HE | !HS/g, '') : name;
  const btnSearch = (check) => {
    saveValue(`keyword=${searchText.value}`);
    saveType(check);
    const searchTxtBox = {
      searchTxt: `keyword=${searchText.value}`,
      check: check,
    };
    store.commit('STATE_UTL', searchTxtBox);
    router.push('/movie');
    searchText.value = '';
  };
  </script>
  
  <style scoped>
  @import '@/css/common.css';
@import '@/css/reset.css';
  </style>
  