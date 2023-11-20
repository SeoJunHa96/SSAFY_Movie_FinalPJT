<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

const logIn = function() {
    const payload = {
        username: username.value,
        password: password.value
    }
    store.logIn(payload)
}

const username = ref(null)
const password = ref(null)
</script>

<template>
    <div>
        <h1>로그인</h1>
        <form @submit.prevent="logIn">
            <label for="username">ID : </label>
            <input type="text" id="username" v-model.trim="username"><br>

            <label for="password">PASSWORD : </label>
            <input type="password" id="password" v-model.trim="password"><br>
            
            <input type="submit" value="login">
        </form>
    </div>
</template>

<style scoped>

</style>
