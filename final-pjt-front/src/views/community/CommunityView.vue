
<template>
    <div>
        <p>{{ store }}</p>
        <RouterLink :to="{ name:'CreateView'}">
        [Create]
        </RouterLink>        
        <ArticleList />
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterView, RouterLink } from 'vue-router'
import ArticleList from '@/components/community/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
    store.getArticles()
})
</script>

<style scoped>

</style>
