<template>
  <div>
    <h1>Detail</h1>
    <div v-if="article">
      <p>제목: {{ article.title }}</p>
      <p>내용: {{ article.content }}</p>
      <p>작성일: {{ article.created_at }}</p>
      <p>수정일: {{ article.updated_at }}</p>
      <hr>
      <div v-if="article.comment_set && article.comment_set.length > 0">
        <h3>댓글</h3>
        <div v-for="comment in article.comment_set" :key="comment.id">
          <CommentList :comment="comment" />
        </div>
      </div>
      <div v-else>
        <p>댓글이 없습니다.</p>
      </div>
      <br>
      <br>
      <br>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'
import CommentList from '@/components/community/CommentList.vue'
import { nextTick } from 'vue'
const store = useCounterStore()
const route = useRoute()
const article = ref(null)
const contentHeight = ref('')

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/community/detail/${route.params.id}/`,
  })
    .then((res) => {
      console.log(res.data)
      article.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
})

const articleDetail = ref(null)

watch(article, async () => {
  // 내용이 일정 영역을 넘어가면 계속 확장되도록 contentHeight를 업데이트
  contentHeight.value = article.value.content.length > 200 ? 'none' : '300px';
  
  // DOM 업데이트를 기다립니다.
  await nextTick()
  
  // 게시글의 높이를 계산하여 블러 효과를 적용한 뒷배경의 높이로 설정
  if (articleDetail.value) {
    const height = articleDetail.value.scrollHeight
    articleDetail.value.style.setProperty('--blur-background-height', `${height}px`)
  }
})

</script>

<style>
/* 필요한 경우 스타일링 추가 */
</style>
