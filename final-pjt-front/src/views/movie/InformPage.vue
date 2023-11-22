<template>
  <div class="main-container">
    <InformConts></InformConts>
    <SimilarMovie></SimilarMovie>
  </div>
</template>
  
<script setup>
  import InformConts from '@/components/InformConts.vue';
  import SimilarMovie from '@/components/SimilarMovie.vue';
</script>
  
<style>
  .main-container {
    margin-left: 50px;
    margin-right: 50px;
}
</style>
    