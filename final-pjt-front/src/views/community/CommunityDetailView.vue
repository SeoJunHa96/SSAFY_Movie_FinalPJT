<template>
  <div class="detail-container">
    <div v-if="article" class="article-detail">
      <br><br><br><br>
      <h1><strong></strong> {{ article.title }}</h1>
      <p><strong>작성일:</strong> {{ article.created_at }}</p>
      <p><strong>수정일:</strong> {{ article.updated_at }}</p>
      <br><br>

      <div v-if="article" class="article-detail" ref="articleDetail">
        {{ article.content }}
      </div>
      <hr class="custom-hr">
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

<style scoped>
.detail-container {
  width: 800px;
  margin: 0 auto;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 19px;
  color: #7c6a56;
  position: relative;
  height: 100vh; /* 브라우저 높이만큼의 높이를 갖도록 변경 */
  
}

h1 {
  font-size: 45px;
  margin-bottom: 20px;
}

.article-detail p {
  margin-bottom: 10px;
}

.article-detail p strong {
  font-weight: bold;
}


.article-content {
  overflow-y: auto; /* 내용이 넘어갈 경우 스크롤 생성 */
  margin-bottom: 20px;
  min-height: 350px;
}

.custom-hr {
  margin: 20px 0;
  border: 0; /* 기본 테두리 제거 */
  border-top: 3px solid #000000; /* 원하는 굵기와 색상으로 변경 */
}



.detail-container::before {
  content: '';
  position: absolute;
  top: -3px;
  left: -15%;
  width: 130%;
  height: var(--blur-background-height, 100%); 
  backdrop-filter: blur(5px);
  z-index: -1;
} 


.article-detail {
  position: relative;
}

.article-detail::before {
  content: '';
  position: absolute;
  top: 0;
  left: -15%;
  width: 130%;
  height: 100%;

  backdrop-filter: blur(5px);
  z-index: -1;
}
</style>
