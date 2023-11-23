<template>
  <div class="write-container">
    <form @submit.prevent="createArticle">
      <div class="input-field">
        <label for="title">제목:</label>
        <input type="text" v-model.trim="title" id="title" placeholder="제목을 입력해주세요">
      </div>
      <div class="input-field">
        <label for="content">내용:</label>
        <textarea v-model.trim="content" id="content" placeholder="영화 관련 주제가 아닐 경우 임의 삭제 될 수 있습니다."></textarea>
      </div>
      <input class="submit-button btn-two green rounded" type="submit" value="작성 완료">
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

<style scoped>
.write-container {
  width: 800px;
  margin: 0 auto;
  font-family: 'Noto Sans KR', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  align-items: center;
  justify-content: flex-start;
  padding-bottom: 75px;
  max-width: 800px;
  margin-top: 50px;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.input-field {
  margin-bottom: 20px;
}

.input-field label {
  display: block;
  margin-bottom: 10px;
  font-weight: bold;
  
}

.input-field input[type="text"],
.input-field textarea {
  width: 100%;
  padding: 15px; /* 큰 크기로 조정 */
  border: none;
  border-radius: 8px; /* 둥근 모서리 적용 */
  background-color: rgba(6, 129, 206, 0.1); /* 파란색 불투명한 배경 */
  margin-bottom: 20px; /* 여백 조정 */
  font-size: 16px; /* 원하는 크기로 조절 */
}

.input-field input[type="text"]::placeholder,
.input-field textarea::placeholder {
  color: #aaa; /* 기본 입력 내용 색상 */
}
.submit-button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  background-color: #0681ce;
  color: white;
  font-size: 16px;
  cursor: pointer;
}
.btn {
  
  margin: 1rem;
}
/* Your previous styles... */

/* Colors for .btn and .btn-two */
.btn.green, .btn-two.green   {background-color: #8e8071;}
/* You can keep the other classes based on your requirement */

.rounded {
  border-radius: 10px;
}

/* Button two - I have no creativity for names */
.btn-two {
  color: white; 
  padding: 15px 25px;
  display: inline-block;
  border: 1px solid rgba(0,0,0,0.21);
  border-bottom-color: rgba(0,0,0,0.34);
  text-shadow:0 1px 0 rgba(0,0,0,0.15);
  font-size: 100%; /* 글자 크기 조정 */
  box-shadow: 0 1px 0 rgba(255,255,255,0.34) inset, 
              0 2px 0 -1px rgba(0,0,0,0.13), 
              0 3px 0 -1px rgba(0,0,0,0.08), 
              0 3px 13px -1px rgba(0,0,0,0.21);
}
.btn-two:active {
  top: 1px;
  border-color: rgba(0,0,0,0.34) rgba(0,0,0,0.21) rgba(0,0,0,0.21);
  box-shadow: 0 1px 0 rgba(255,255,255,0.89),0 1px rgba(0,0,0,0.05) inset;
  position: relative;
}

</style>
