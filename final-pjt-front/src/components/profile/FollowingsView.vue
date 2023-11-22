<template>
    <div>
      <a class="link m-0 fw-bold fs-3" :href="urls">{{ user.username }}</a>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  
  const user = ref([])
  const urls = ref(`http://localhost:8080/profile/${props.userId}/`)
  
  const getUser = () => {
    axios({
      method: 'get',
      url: `${API_URL}/userinfo/${props.userId}/`,
    })
      .then(res => {
        user.value = res.data
      })
  }
  
  const goProfile = () => {
    router.push({ name: 'Profile', params: { user_pk: props.userId }})
  }
  
  onMounted(() => {
    getUser()
  })
  
  defineProps({
    userId: Number
  })
  </script>
  
  <style>
  
  </style>