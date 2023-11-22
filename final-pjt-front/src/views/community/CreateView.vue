<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title">
      </div>
      <div>
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content"></textarea>
      </div>
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { ref } from 'vue'

const store = useCounterStore()
const title = ref(null)
const content = ref(null)

const createArticle = () => {
  const payload = {
    title: title.value,
    content: content.value
  }
  store.createArticle(payload)
}
</script>

<style>

</style>
