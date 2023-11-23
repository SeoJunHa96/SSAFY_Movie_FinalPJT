<template>
    <div class="container">
      <div class="table-wrapper">
        <table id="table_board" class="list">
        <colgroup>
          <col width="150">
          <col width="60%">
          <col width="250">
        </colgroup>
        <thead>
          <tr style="text-align: center;">
            <th>번호</th>
            <th>제목</th>
            <th>날짜</th>
          </tr>
        </thead>
        <tbody>
          <ArticleListItem
            v-for="article in store.articles"
            :key="article.id"
            :article="article"
          />
        </tbody>
          <tr>
          </tr>
        </table>
    </div>
  </div>
</template>
  
  <script setup>
  import ArticleListItem from '@/components/community/ArticleListItem.vue'
  import { useCounterStore } from '@/stores/counter'
  import { RouterLink } from 'vue-router'
  
  const store = useCounterStore()
  </script>
  
  <style scoped>
  /* 아티클 리스트에 대한 스타일은 여기에 추가하세요. */
  .container {
  display: flex;
  justify-content: center;
}

.table-wrapper {
  width: 180%;
  display: flex;
  justify-content: center;
}

#table_board {
  border-radius: 15px;
  border-spacing: 0px;
  overflow: hidden;
  font-size: 21px;
  color: #8e8071;
  width: 100%;
}

  #table_board th {
    background-color: #b1a599;
    color: white;
    height: 25px;
    font-size: 24px;
    -webkit-text-stroke: 1px rgba(255, 255, 255, 0.1);
    font-weight: 400;
    padding: 10px;
    padding-left: 15px;
  }
  
  #table_board tr td:nth-child(2),
  #table_board tfoot tr td {
    text-align: left;
    padding-left: 10px;
  }
  
  #table_board tbody td {
    padding: 10px;
    text-align: center;
    background-color: white;
    border-left: 1px solid gray;
    border-bottom: 1px solid gray;
  }
  
  #table_board tbody td:first-child {
    border-left: 0px;
  }
  
  #table_board tfoot tr td {
    background-color: #efe8e2;
    color: white;
    height: 50px;
    padding-left: 40px;
  }
  
  #table_board tfoot a {
    color: black;
  }
  
  #table_board.list tbody a {
    color: #8e8071;
  }
  
  #table_board.list tbody a:link {
    color: #8e8071;
  }
  
  #table_board.list tbody a:visited {
    color: #8e8071;
  }
  
  #table_board.list tbody a:hover {
    color: #0681ce;
  }
  
  #table_board.list tbody a:active {
    color: #8e8071;
  }
  
  #table_board.list tbody tr:hover * {
    color: #0681ce !important;
  }
  
  #table_board tr:hover {
    background-color: transparent;
  }
  
  #table_board tr:hover td {
    background-color: white;
    color: #8e8071;
    cursor: pointer;
  }
  </style>
  