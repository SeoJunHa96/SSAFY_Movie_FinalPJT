<script setup>
defineProps({
    comment: Object
})
</script>

<template>
    <div>
        <h5>{{ comment.user.username }}</h5>
        <p>{{ comment.content }}</p>
        <p>{{ comment.content }}</p>
    </div>
</template>

<style scoped>

</style>
