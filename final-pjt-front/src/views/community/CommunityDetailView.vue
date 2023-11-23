<template>
  <div class="detail-container">
    <h1>Detail</h1>
    <div v-if="article" class="article-detail">
      <p><strong>제목:</strong> {{ article.title }}</p>
      <p><strong>작성일:</strong> {{ article.created_at }}</p>
      <p><strong>수정일:</strong> {{ article.updated_at }}</p>

      <p style="margin-bottom: 150px;"><strong>내용:</strong> {{ article.content }}</p>
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
</script>

<style scoped>

.detail-container {
  width: 800px;
  margin: 0 auto;
  font-family: 'Noto Sans KR', sans-serif;
  color: #8e8071;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.article-detail p {
  margin-bottom: 10px;
}

.article-detail p strong {
  font-weight: bold;
}

.article-detail hr {
  margin: 20px 0;
  border-color: #8e8071;
}

.article-detail h3 {
  font-size: 20px;
  margin-bottom: 10px;
}
</style>
