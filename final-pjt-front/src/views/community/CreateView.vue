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
<template>
  <div class="write-container">
    <form @submit.prevent="createArticle">
      <div class="input-field">
        <label for="title" style="font-size: 25px;">제목</label>
        <input type="text" v-model.trim="title" id="title" placeholder="제목을 입력해주세요" class="custom-title">
      </div>
      <div class="input-field">
        <label for="content" style="font-size: 22px;">내용</label>
        <textarea v-model.trim="content" id="content" placeholder="영화 관련 주제가 아닐 경우 임의 삭제 될 수 있습니다." class="custom-textarea"></textarea>
      </div>
      <div class="submit-button-container">
        <input class="submit-button btn-two green rounded" type="submit" value="작성 완료">
      </div>
    </form>
  </div>
</template>

<style scoped>
.write-container {
  width: 100%;
  margin: 0 auto;
  font-family: 'Noto Sans KR', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding-bottom: 75px;
  max-width: 800px;
  margin-top: 50px;
}

.h1 {
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
  padding: 13px; 
  border: none;
  border-radius: 8px; 
  background-color: rgb(255, 255, 255); 
  margin-bottom: 20px; 
  font-size: 21px; 
}

.input-field input[type="text"]::placeholder,
.input-field textarea::placeholder {
  color: #868686;
}
.custom-title{
  width: 100%; /* 수정된 부분: 화면 가운데 정렬을 위해 100%로 변경 */
  min-width: 800px;
  max-width: 1000px;/* 적절한 최대 너비로 설정 */
}
.custom-textarea {
  resize: none; 
  height: 300px; 
  width: 100%; /* 수정된 부분: 화면 가운데 정렬을 위해 100%로 변경 */
  min-width: 800px;
  max-width: 1000px; /* 적절한 최대 너비로 설정 */
}
.submit-button-container {
  display: flex;
  justify-content: flex-end;
  align-items: center;
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

.btn.green,
.btn-two.green {
  background-color: #8e8071;
}

.rounded {
  border-radius: 10px;
}

.btn-two {
  color: white;
  padding: 15px 25px;
  display: inline-block;
  border: 1px solid rgba(0, 0, 0, 0.21);
  border-bottom-color: rgba(0, 0, 0, 0.34);
  text-shadow: 0 1px 0 rgba(0, 0, 0, 0.15);
  font-size: 100%;
  box-shadow: 0 1px 0 rgba(255, 255, 255, 0.34) inset, 0 2px 0 -1px rgba(0, 0, 0, 0.13),
    0 3px 0 -1px rgba(0, 0, 0, 0.08), 0 3px 13px -1px rgba(0, 0, 0, 0.21);
}
.btn-two:active {
  top: 1px;
  border-color: rgba(0, 0, 0, 0.34) rgba(0, 0, 0, 0.21) rgba(0, 0, 0, 0.21);
  box-shadow: 0 1px 0 rgba(255, 255, 255, 0.89), 0 1px rgba(0, 0, 0, 0.05) inset;
  position: relative;
}
</style>
