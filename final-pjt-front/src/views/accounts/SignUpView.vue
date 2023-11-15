<template>
    <div>
        <h1>회원 가입</h1>
        <form @submit.prevent="signUp">
            <label for="username">이름 : </label> <br>
            <input type="text" id="username" v-model.trim="username"><br>
            <br>
            <label for="nickname">활동명 : </label><br>
            <input type="text" id="nickname" v-model.trim="nickname"><br>
            <br>
            <label for="password1">비밀번호 : </label><br>
            <input type="password" id="password1" v-model.trim="password1"><br>
            <br>
            <label for="password2">비밀번호 확인 : </label><br>
            <input type="password" id="password2" v-model.trim="password2"><br>
            <br>
            <label for="sign_like_movie">가장 재미있게 본 영화는 무엇입니까? : </label><br>
            <input type="text" id="sign_like_movie" v-model.trim="sign_like_movie"><br>
            <br>
            <label for="like_genre">가장 좋아하는 영화 장르는 무엇입니까? : </label><br>
            <input type="text" id="like_genre" v-model.trim="like_genre"><br>
            <br>
            <input type="submit" value="SignUp">
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const username = ref(null)
const nickname = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const sign_like_movie = ref(null)
const like_genre = ref(null)

const handleSubmit = () => {
  // 여기에 회원 가입 처리 로직을 추가하세요.
}
</script>

<style scoped>
/* 추가적인 스타일링이 필요하다면 여기에 추가하세요. */
</style>
