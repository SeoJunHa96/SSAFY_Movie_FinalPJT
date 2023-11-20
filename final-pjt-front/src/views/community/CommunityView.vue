
<template>
    <div>
        영화 리뷰 커뮤니티 화면
        <ArticleList />
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterView } from 'vue-router'
import ArticleList from '@/components/community/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
    store.getArticles()
})
</script>

<style scoped>

</style>
