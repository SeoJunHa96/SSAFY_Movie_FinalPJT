<template>
    <div class="container">
        <ArticleList />
        <RouterLink :to="{ name:'CreateView'}">
          <button class="buttonmargin btn-two green rounded" style="align-items: flex-start;">글쓰기</button>
        </RouterLink>        
    </div>
  </template>   
  
  <script setup>
  import { onMounted } from 'vue'
  import { useCounterStore } from '@/stores/counter'
  import { RouterView, RouterLink } from 'vue-router'
  import ArticleList from '@/components/community/ArticleList.vue'
  
  const store = useCounterStore()
  
  onMounted(() => {
    store.getArticles()
  })
  </script>
  
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  align-items: center;
  justify-content: flex-start;

  padding-bottom: 75px;
  max-width: 800px;
  margin-top: 50px;
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
  font-size: 120%; /* 글자 크기 조정 */
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
  