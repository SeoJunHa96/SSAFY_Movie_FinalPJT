<template>
  <div class="mainConts">
    <form class="checkbox">
      <label 
        v-for="(item, index) in searchType" :key="index"
        :class="{'checkStyle': check === item.type}">
        <input 
          type="radio"  name="search"
          v-model="check" :value="item.type" />
        {{ item.typeKR }}
      </label>
    </form>

    <form class="inputBox" @submit.prevent="submitSearchData">
      <input 
        v-for="(item, index) in filteredSearchType" :key="index"
        v-model="searchText"
        type="text" :placeholder="`${item.typeKR} 입력하세요`" />
      <button>검색</button>
    </form> 
  </div>
</template>

<script setup>
import { ref, onMounted, inject, computed } from 'vue';
import { useRouter } from 'vue-router';
import store from '@/store/index.js'
import { saveValue, saveType, deleteCookie } from '@/utils/cookies.js';
const eventbus = inject('eventbus');

const searchType = [
  { type: 'title', typeKR: '제목' },
  { type: 'actor', typeKR: '배우' },
  { type: 'director', typeKR: '감독' },
  { type: 'nation', typeKR: '국가' },
];

const searchText = ref('');
const check = ref('title');
const router = useRouter();


onMounted(() => {
  deleteCookie('movie_title');
  deleteCookie('movie_type'); 
});

const filteredSearchType = computed(() => {
  return searchType.filter(item => item.type === check.value);
});

const submitSearchData = () => {
  eventbus.passSearchTxt(searchText.value, check.value);

  saveValue(`${check.value}=${searchText.value}`);
  saveType(check.value);           

  const searchTxtBox = {
    searchTxt : `${check.value}=${searchText.value}`, 
    check : check.value
  };

  store.commit('STATE_UTL', searchTxtBox);

  router.push('/moviepage');

  searchText.value = '';
};
</script>

<style scoped>
@import '@/css/common.css';
@import '@/css/reset.css';
</style>
