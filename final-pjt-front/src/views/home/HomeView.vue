<template>
  <div class="main-container">
    <div>
      <h1>지금 상영 중인 영화</h1>
      <Swiper
        :modules="swiperOptions.modules"
        :centered-slides="true"
        :loop="true"
        :slides-per-view="swiperOptions.slidesPerView"
        :space-between="swiperOptions.spaceBetween"
        :navigation="swiperOptions.navigation"
        @swiper="swiperOptions.onSwiper"
        @slideChange="swiperOptions.onSlideChange"
      >
      <SwiperSlide  v-for="movie in newMovies" :key="movie.id">
        <HomeMovieCard
          :key="movie.id"
          :movie="movie"
        />
      </SwiperSlide>      
      </Swiper>
      <br><br>
      <h1>곧 개봉될 영화</h1>
      <Swiper
        :modules="swiperOptions.modules"
        :centered-slides="true"
        :loop="true"
        :slides-per-view="swiperOptions.slidesPerView"
        :space-between="swiperOptions.spaceBetween"
        :navigation="swiperOptions.navigation"
        @swiper="swiperOptions.onSwiper"
        @slideChange="swiperOptions.onSlideChange"
      >
      <SwiperSlide  v-for="movie in upcomingMovies" :key="movie.id">
        <HomeMovieCard
          :key="movie.id"
          :movie="movie"
        />
      </SwiperSlide>      
      </Swiper>      
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, computed } from 'vue';
import router from '@/router';
import HomeMovieCard from '@/components/home/HomeMovieCard.vue';
import 'swiper/swiper-bundle.css';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Navigation } from 'swiper';

// swiper 관련1
const onSwiper = (swiper) => {
};

// swiper 관련2
const onSlideChange = () => {
  console.log('slide change');
};

// swiper 관련3
const swiperOptions = {
  modules: [Navigation],
  slidesPerView: 4,
  spaceBetween: 50,
  navigation: true,
  onSwiper,
  onSlideChange,
};

const apiKey = '3691eda9c0d72053e1652d747c826899';
const currentDate = new Date();
const tomorrowDate = new Date(currentDate.getTime() + (24 * 60 * 60 * 1000)); // 현재 날짜로부터 1일 후 날짜 계산
const pastDate = new Date(currentDate.getTime() - (7 * 24 * 60 * 60 * 1000)); // 현재 날짜로부터 1주 이전 날짜 계산
const futureDate = new Date(currentDate.getTime() + (7 * 24 * 60 * 60 * 1000)); // 현재 날짜로부터 1주 후 날짜 계산

const newMovies = ref([]);
const upcomingMovies = ref([]);
const moviesData = ref([]);
const loading = ref(true);

const formatDate = (date) => {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
};

const fetchNewMovies = async () => {
  const apiUrl = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&region=KR&release_date.gte=${formatDate(pastDate)}&release_date.lte=${formatDate(currentDate)}&api_key=${apiKey}`;

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    newMovies.value = data.results;
    loading.value = false
    // New Movies 데이터를 처리하는 로직을 작성하세요.
  } catch (error) {
    console.error('데이터 불러오기 오류:', error);
  }
};

const fetchUpcomingMovies = async () => {
  const apiUrl = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&region=KR&release_date.gte=${formatDate(tomorrowDate)}&release_date.lte=${formatDate(futureDate)}&api_key=${apiKey}`;

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    upcomingMovies.value = data.results;
    loading.value = false
  } catch (error) {
    console.error('데이터 불러오기 오류:', error);
  }
};

onMounted(() => {
  fetchNewMovies();
  fetchUpcomingMovies();
});

</script>

<style scoped>
.movie-item {
  flex: 0 0 calc(20% - 20px); /* 5개 아이템을 한 줄에 배치하기 위한 스타일 */
  margin: 10px;
}

.movie-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between; /* 5개 아이템을 한 줄에 배치하기 위한 스타일 */
}

.movie-card {
  position: relative;
  border: 1px solid #ddd;
  padding: 10px;
  text-align: center;
}

.movie-poster {
  max-width: 200px; /* 포스터 최대 너비 */
  height: auto;
  display: block;
  margin: 0 auto; /* 가운데 정렬 */
}

.movie-info {
  display: none;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 10px;
}

.movie-card:hover .movie-info {
  display: block;
}

.main-container {
  margin-left: 20px;
  margin-right: 20px;
}
</style>
