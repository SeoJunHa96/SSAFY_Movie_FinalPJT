<script setup>
import { useCounterStore } from '@/stores/counter'
import axios from 'axios'

const store = useCounterStore()

const logOut = () => {
    store.logOut()
}
</script>

<template>
    <div>
        <h1>로그아웃</h1>
        <button @click="logOut">로그아웃</button>
    </div>
</template>

<style scoped>
/* 스타일링 내용 */
</style>
