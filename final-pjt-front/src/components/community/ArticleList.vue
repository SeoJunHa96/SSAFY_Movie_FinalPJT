<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/community/ArticleListItem.vue'

const store = useCounterStore()
</script>

<template>
    <div>
        <h3>Article List</h3>
        <ArticleListItem
        v-for="article in store.articles"
        :key="article.id"
        :article="article"
         />
    </div>
</template>

<style scoped>

</style>
