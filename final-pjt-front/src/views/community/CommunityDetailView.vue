<template>
  <div>
    <h1>Detail</h1>
  <div v-if="article">
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <p>작성일: {{ article.created_at }}</p>
    <p>수정일: {{ article.updated_at }}</p>
    <hr>
    <div v-if="article.comment_set">
      <h3>댓글</h3>
      <div v-for="comment in article.comment_set" :key="comment.id">
        <CommentList :comment="comment" />
      </div>
    </div>
    <div v-else>
      <p>로딩중</p>
    </div>
  </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'
import CommentList from '@/components/community/CommentList.vue'

const store = useCounterStore()
const route = useRoute()
const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/community/articles/${route.params.id}/`,
  })
    .then((res) => {
      console.log(res.data)
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)

    })
})

</script>

<style>

</style>
