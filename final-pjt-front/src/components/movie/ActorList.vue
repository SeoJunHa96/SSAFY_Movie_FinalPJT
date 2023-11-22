<script setup>
import router from '@/router';
defineProps({
    actor: Object
})

const getProfileUrl = (relativePath) => {
    if (relativePath) {
      return `https://image.tmdb.org/t/p/w200${relativePath}`;
    }
    return '';
  };


const goActor = (actor) => {
    router.push(`/actors/${actor.id}`);
  };
</script>

<template>
    <div v-if="actor" @click="goActor(actor)">
        <img :src="getProfileUrl(actor.profile_path)" alt="actor_img">
        <p>{{ actor.name }}</p>
    </div>
    <div v-else>로딩중</div>
</template>

<style scoped>

</style>
