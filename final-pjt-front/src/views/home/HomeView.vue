<template>
  <div>

    <div>
      <h1>지금 상영중인 영화</h1>
      <swiper
        class="swiper"
        :modules="modules"
        :pagination="true"
        :effect="'coverflow'"
        :grab-cursor="true"
        :centered-slides="true"
        :slides-per-view="'auto'"
        :coverflow-effect="{
          rotate: 50,
          stretch: 0,
          depth: 100,
          modifier: 1,
          slideShadows: true
        }"
      >
        <swiper-slide v-for="movie in movies" :key="movie.id">
          <img :src="getImageUrl(movie.poster_path)" alt="movie_poster" />
        </swiper-slide>
        <!-- <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div> -->
      </swiper>
      <div v-if="loading">로딩 중...</div>
      <div v-else class="movie-list">
        <div class="movie-row" v-for="(movieRow, rowIndex) in movieChunks" :key="rowIndex">
          <div v-for="movie in movieRow" :key="movie.id" class="movie-item">
            <div class="movie-card" @mouseenter="toggleCard(movie.id)" @mouseleave="toggleCard(null)" @click="goDetail(movie)">
              <img :src="getImageUrl(movie.poster_path)" alt="Movie Poster" class="movie-poster" />
              <div class="movie-info" v-if="hoveredMovie === movie.id">
                <h3>{{ movie.title }}</h3>
                <p>개봉 : {{ movie.release_date }}</p>
                <p>평점 : {{ movie.vote_average }}</p>
                <p>줄거리: {{ movie.overview }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="search-bar" style="display: flex; justify-content: center; width: 100%; height: 40px; border: none; background-color: #fff;">
      <input type="text" class="input" style="border: none; height: 40px; width: 500px;" placeholder="제목, 배우, 감독 등으로 검색하세요.">
      <button type="submit" class="submit" style="width: 70px; height: 40px; background-color: #000; color: ; border-radius: 10px;">부트스트랩 아이콘으로 바꿀꺼야</button>
      </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import router from '@/router';
import 'swiper/swiper-bundle.css';
import { Swiper, SwiperSlide } from 'vue-awesome-swiper';

const movies = ref([]);
const loading = ref(true);
const hoveredMovie = ref(null);

const fetchTopRatedMovies = async () => {
  const apiKey = '3691eda9c0d72053e1652d747c826899';
  const apiUrl = `https://api.themoviedb.org/3/movie/now_playing?api_key=${apiKey}&language=ko-KR`;

  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    movies.value = data.results.slice(0, 10); // 처음부터 10개만 가져오도록 수정
    loading.value = false;
  } catch (error) {
    console.error('데이터 불러오기 오류:', error);
    loading.value = false;
  }
};

onMounted(() => {
  fetchTopRatedMovies();
});

const getImageUrl = (relativePath) => {
  if (relativePath) {
    return `https://image.tmdb.org/t/p/w500${relativePath}`;
  }
  return '';
};

const toggleCard = (id) => {
  hoveredMovie.value = id;
};

const goDetail = (movie) => {
  router.push(`/movies/${movie.id}`);
};

const searchTerm = ref('');
const searchResults = ref([]);

const search = () => {
  // 검색어를 API에 전달하여 검색 결과를 가져옵니다.
  const apiKey = '3691eda9c0d72053e1652d747c826899';
  const apiUrl = `https://api.themoviedb.org/3/search/movie?api_key=${apiKey}&language=ko-KR&query=${searchTerm.value}`;
  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      searchResults.value = data.results;
    });
};

// 5개씩 아이템을 묶어서 보여주기 위한 계산된 속성 추가
const movieChunks = computed(() => {
  const chunkSize = 5;
  const result = [];
  for (let i = 0; i < movies.value.length; i += chunkSize) {
    result.push(movies.value.slice(i, i + chunkSize));
  }
  return result;
});

const swiperOptions = {
  slidesPerView: 1,
  pagination: { 
      el: '.swiper-pagination', 
      clickable: true 
  }, 
  navigation: { 
      nextEl: '.swiper-button-next', 
      prevEl: '.swiper-button-prev' 
  } 
}
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
</style>
