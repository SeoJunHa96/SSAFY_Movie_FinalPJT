<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

onMounted(() => {
    store.getArticles()
})
</script>

<template>
    <div>
        영화 리뷰 커뮤니티 화면
    </div>
</template>

<style scoped>

</style>
