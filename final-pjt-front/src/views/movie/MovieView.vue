<template>
  <div class="main-container">
    <div class="content-container">
      <InputSearchForm></InputSearchForm>
      <GenreSearchBtns></GenreSearchBtns>
    </div>
  </div>
</template>
  
<script setup>
  import InputSearchForm from '@/components/search/InputSearchForm.vue';
  import GenreSearchBtns from '@/components/search/GenreSearchBtns.vue';
</script>
  
<style scoped>
@import '@/css/common.css';
@import '@/css/reset.css';

.main-container {
  background-color: rgba(0, 0, 0, 0.5);
  width: 600px;
  height: 500px;
  margin: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  /* border: 1px solid black; */
  border-radius: 10px;
}

.content-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>