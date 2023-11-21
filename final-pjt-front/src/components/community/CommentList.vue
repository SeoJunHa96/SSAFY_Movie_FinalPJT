<script setup>
defineProps({
    comment: Object
})
</script>

<template>
    <div v-if="comment">
        <p>{{ comment.user.username }} - {{ comment.content }}</p>
        <p>{{ comment.user.pk }}</p>
        <p>{{ store }}</p>
        <!-- <p>{{ currenUser }}</p> -->
        
        <!-- <button v-if="currentUser && comment.user.pk == currenUser.pk">수정</button>
        <button v-if="currentUser && comment.user.pk == currenUser.pk">삭제</button> -->
    </div>
    <div v-else>로딩중</div>
</template>

<style scoped>

</style>
