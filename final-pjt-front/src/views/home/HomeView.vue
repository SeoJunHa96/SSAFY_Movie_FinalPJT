<template>
  <div class="main-container">
    <div>
      <h1>최근 개봉한 영화</h1>
      <Swiper
        class="movie-list"
        :modules="swiperOptions.modules"
        :centered-slides="true"
        :loop="true"
        :slides-per-view="swiperOptions.slidesPerView"
        :space-between="swiperOptions.spaceBetween"
        :navigation="swiperOptions.navigation"
        :autoplay="swiperOptions.autoplay"
        @swiper="swiperOptions.onSwiper"
        @slideChange="swiperOptions.onSlideChange"
      >
      <SwiperSlide  v-for="movie in newMovies" :key="movie.id">
        <HomeMovieCard
          v-if="movie.poster_path"
          :key="movie.id"
          :movie="movie"
        />
      </SwiperSlide>      
      </Swiper>
      <br><br>
      <h1>곧 개봉될 영화</h1>
      <Swiper
        class="movie-list"
        :modules="swiperOptions.modules"
        :centered-slides="true"
        :loop="true"
        :slides-per-view="swiperOptions.slidesPerView"
        :space-between="swiperOptions.spaceBetween"
        :navigation="swiperOptions.navigation"
        :autoplay="swiperOptions.autoplay"
        @swiper="swiperOptions.onSwiper"
        @slideChange="swiperOptions.onSlideChange"
      >
      <SwiperSlide  v-for="movie in upcomingMovies" :key="movie.id">
        <HomeMovieCard
          v-if="movie.poster_path"
          :key="movie.id"
          :movie="movie"
        />
      </SwiperSlide>      
      </Swiper>      
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import HomeMovieCard from '@/components/home/HomeMovieCard.vue';
import 'swiper/swiper-bundle.css';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Autoplay, Navigation } from 'swiper';

// swiper 관련1
const onSwiper = (swiper) => {
  // console.log(swiper);
};

// swiper 관련2
const onSlideChange = () => {
  // console.log('slide change');
};

// swiper 관련3
const swiperOptions = {
  modules: [Navigation, Autoplay],
  slidesPerView: 4,
  spaceBetween: 50,
  navigation: true,
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
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
    newMovies.value = data.results.filter(movie => movie.poster_path);
    loading.value = false
  } catch (error) {
    console.error('데이터 불러오기 오류:', error);
  }
};

const fetchUpcomingMovies = async () => {
  const apiUrl = `https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=ko-KR&region=KR&release_date.gte=${formatDate(tomorrowDate)}&release_date.lte=${formatDate(futureDate)}&api_key=${apiKey}`;

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    upcomingMovies.value = data.results.filter(movie => movie.poster_path);
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
.main-container {
  margin-left: 50px;
  margin-right: 50px;
}
h1 {
  margin-top: 50px;
  margin-bottom: 25px;
}
.movie-list {
  padding-top: 10px;
  padding-bottom: 10px;
  border-top: 1px solid black;
  border-bottom: 1px solid black;
  background-color: rgba(0, 0, 0, 0.1)
}
</style>
