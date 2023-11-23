<template>
  <div class="genreBtnBox">
    <form class="genreBtn" @click="btnSearch('genreCK')" v-bind:value="'genreCK'">
      <p>
        <span># genre</span> 
        <span># 장르</span>
        <span># 추천</span>
      </p>
      <button v-for="(item, index) in genre" :key="index" @click="searchText = item" class="btn btn-ghost">
        {{ item }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import store from '@/store/index.js'
import { useRouter } from 'vue-router';
import { saveValue, saveType } from '@/utils/cookies.js';

const genre = ref(['애니메이션', '역사', '코메디', '드라마', 'SF', '사회', '액션', '로맨스']);
const searchText = ref('');

const router = useRouter();

const btnSearch = (check) => {
  saveValue(`genre=${searchText.value}`);
  saveType(check);

  const searchTxtBox = {
    searchTxt : `genre=${searchText.value}`, 
    check : check,
  };
  console.log(searchTxtBox);

  store.commit('STATE_UTL', searchTxtBox);

  router.push('/moviepage');

  searchText.value = '';
}


</script>

<style scoped>
@import '@/css/common.css';
@import '@/css/reset.css';
</style>