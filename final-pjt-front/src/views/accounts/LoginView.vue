<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const username = ref(null)
const password = ref(null)

const logIn = function() {
    const payload = {
        username: username.value,
        password: password.value
    }
    store.logIn(payload)
}


</script>

<template>
    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
    <div>
        <div class="app-contnet">
            <div class="form-box">
                    <h1>로그인</h1>
                    <br>
                <form @submit.prevent="logIn">
                    <div class="form-group">
                        <label for="username">아이디</label>
                        <input class="placeholdercolor" placeholder="아이디를 입력하세요." type="text" id="username" v-model.trim="username">
                    </div>
                    <div class="form-group">
                        <label for="password">비밀번호</label>
                        <input class="placeholdercolor" placeholder="비밀번호를 입력하세요." type="password" id="password" v-model.trim="password"><br>
                    </div>
                    <br>
                    <button type="submit" value="login">LOGIN</button>
                </form>
            </div>
        </div>

    </div>
</template>

<style scoped>
/* Signup & Login form styles */
.form-box {
  width: 500px;
  margin: 0 auto;
  font-family: 'Poppins', sans-serif;
  color: #fff;
  width: 100%;
}

.signup-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.form-group{
    display: flex;
  flex-direction: column;
}
.login-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

h1 {
  font-size: 32px;
  font-weight: 600;
  padding-bottom: 30px;
  text-align: center;
  color: white;
}

form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

label {
  font-size: 18px;
  font-weight: 500;
}

input[type="text"],
input[type="password"] {
  padding: 10px;
  border-radius: 5px;
  border: none;
  border-bottom: 2px solid #fff;
  background-color: transparent;
  color: #fff;
  font-size: 16px;
}

input[type="text"]:focus,
input[type="password"]:focus {
  outline: none;
  border-bottom: 2px solid #3498db;
}

button {
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #3498db;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s ease;
  font-size: 18px;
}

button:hover {
  background-color: #2980b9;
}

.placeholdercolor::placeholder {
  color: white;
}
.app-contnet{
    font-family: poppins;
    background-color: rgba(0, 0, 0, 0.5);
    margin: auto auto;
    padding: 40px;
    border-radius: 5px;
    box-shadow: 0 0 10px #000;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 600px;
    height: 500px;
    justify-content: center; /* 수평 가운데 정렬 */
    align-items: center; /* 수직 가운데 정렬 */
}
</style>
