<template>
    <div class="container" style="padding-top:48px;padding-left:48px;">
      <div class="container" style="margin-bottom:30px">
        <div class="row">
            <div class="well profile">
              <div class="row">
                <div class="col-sm-3 col-12">
                </div>
                <div class="col-sm-9 col-12">
                  <div class="col-12 d-flex justify-content-around">
                    <h1 class="title-font fw-bold" style="margin-bottom: 30px"><span style="font-size:5rem;">{{ user.nickname }}</span> 님의 프로필</h1>
                  </div>
                  <div class="col-sm-12 divider text-center row d-flex justify-content-around">
                    <div class="col-sm-3 col-12 follow-info" @click="open1">
                      <h2 class="fw-bold" style="font-size:3rem;">{{followersLength}}</h2>                    
                      <p>팔로워</p>
                    </div>
                    <div class="col-sm-3 col-12 follow-info"  @click="open2">
                      <h2 class="fw-bold" style="font-size:3rem;">{{followingsLength}}</h2>                    
                      <p>팔로잉</p>
                    </div>
                </div>
              </div>
              <div class="row ms-4 py-4">
                <div v-if="isFollowing" class="">{{ user.username }}님을 팔로우 중 입니다.</div>
                <div v-else><br></div>
              </div>    
              <div class="row mx-2">
                <div v-if="isLogin">
                  <div v-if="me.username === user.username">
                    <!-- <br> -->
                  </div>
                  <div class="py-2" v-else>
                    <div class="d-grid gap-2 col-3 mx-auto">
                      <button v-if="isFollowing" @click="follow" class="btn btn-secondary">언팔로우</button>
                      <button v-else @click="follow" class="btn btn-primary">팔로우</button>
                    </div>
                  </div>
                </div>
              </div>        
            </div>
          </div>                 
        </div>
      </div>
      <!-- 팔로잉 모달 -->
      <b-modal
        hide-footer
        v-model="show2"
        id="review-modal"
        size="sm"
        title="팔로잉"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
        :body-bg-variant="bodyBgVariant"
        :body-text-variant="bodyTextVariant"
        :footer-bg-variant="footerBgVariant"
        :footer-text-variant="footerTextVariant"
      >
        <section class="page-section" id="contact">
          <div class="control-group">
              <div v-for="(userId, idx) in user.followings" :key="idx" style="cursor:pointer" class="content-font form-group floating-label-form-group controls mb-0 pb-2">
                  <FollowingsView :userId="userId" />
              </div>
          </div>
        </section>
      </b-modal>
      <!-- 팔로잉 모달 끝 -->
  
      <!-- 팔로워 모달 -->
      <b-modal
        hide-footer
        v-model="show1"
        id="review-modal"
        size="md"
        title="팔로워"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
        :body-bg-variant="bodyBgVariant"
        :body-text-variant="bodyTextVariant"
        :footer-bg-variant="footerBgVariant"
        :footer-text-variant="footerTextVariant"
      >
        <section class="page-section" id="contact">
          <div class="control-group">
              <div v-for="(userId, idx) in user.followers" :key="idx" style="cursor:pointer" class="content-font form-group floating-label-form-group controls mb-0 pb-2">
                  <FollowersView :userId="userId" />
              </div>
          </div>
        </section>
      </b-modal>
      <!-- 팔로워 모달 끝 -->
    </div>
  </template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import FollowersView from "@/components/profile/FollowersView.vue";
import FollowingsView from "@/components/profile/FollowingsView.vue";
import store from '@/store/index.js'
const API_URL = "http://127.0.0.1:8000";

const me = ref([]);
const user = ref([]);
const show1 = ref(false);
const show2 = ref(false);
const variants = ref(["light", "dark"]);
const headerBgVariant = ref("dark");
const headerTextVariant = ref("white");
const bodyBgVariant = ref("dark");
const bodyTextVariant = ref("white");
const footerBgVariant = ref("danger");
const footerTextVariant = ref("dark");
const likeMovies = ref([]);
const reviewMovies = ref([]);
const isLogin = ref(false); 
const isFollowing = ref(false); 


const getMe = () => {
  if (store.getters.isLogin) {
    return;
  }
  axios({
    method: "get",
    url: `${API_URL}/accounts/user/`,
    headers: {
      Authorization: `Token ${store.state.token}`,
    },
  }).then((res) => {
    me.value = res.data;
    getMyName(res.data.pk);
  });
};

const getMyName = (my_pk) => {
  axios({
    method: "get",
    url: `${API_URL}/userinfo/user/${my_pk}/`,
  }).then((res) => {
    user.value = res.data;
    getUserMovies(res.data.like_movies, res.data.reviews);
  });
};

const getUserMovies = (like_movies, reviews) => {
  axios({
    method: "post",
    url: `${API_URL}/movies/${user.value.id}/like/review/`,
    data: {
      like_movies,
      reviews,
    },
    headers: {
      Authorization: `Token ${store.state.token}`,
    },
  }).then((res) => {
    likeMovies.value = res.data[0];
    reviewMovies.value = res.data[1];
  });
};

const open1 = () => {
  show1.value = true;
};

const open2 = () => {
  show2.value = true;
};

const close = () => {
  show1.value = false;
};

const close2 = () => {
  show2.value = false;
};

const followingsLength = () => {
  if (user.value.followings) {
    return user.value.followings.length;
  } else {
    return 0;
  }
};

const followersLength = () => {
  if (user.value.followers) {
    return user.value.followers.length;
  } else {
    return 0;
  }
};

onMounted(() => {
  getMe();
});
</script>


<style scoped>

</style>
