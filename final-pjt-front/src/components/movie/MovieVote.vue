<template>
  <div>
    <h3>TOP 10</h3>

    <div class="top-five" @click="goDetail(movie)" v-for="(movie, index) in topTenMovies.slice(0, 5)" :key="index">
        <img :src="getImageUrl(movie.poster_path)" alt="Movie Poster" class="top-movie-poster" />
        <br>
        <strong class="movie-title">{{ movie.title }}</strong>
        <br>
        평점: {{ movie.vote_average }}
    </div>
    <br><br>

    <div class="other-five" @click="goDetail(movie)" v-for="(movie, index) in topTenMovies.slice(5, 10)" :key="index">
      <img :src="getImageUrl(movie.poster_path)" alt="Movie Poster" class="top-movie-poster" />
      <br>
      <strong class="movie-title">{{ movie.title }}</strong>
      <br>
      평점: {{ movie.vote_average }}
    </div>
    <hr>
    <h3>TOP 100</h3>

    <div class="other-movies">
  <div class="seven-movies-per-line" v-for="(movieGroup, groupIndex) in groupedOtherMovies" :key="groupIndex">
    <div class="seven-movies-row">
      <div v-for="(movie, index) in movieGroup" @click="goDetail(movie)" :key="index" class="other-movie-item" @mouseover="toggleFlip(movie)">
        <div class="movie-poster-container" :class="{ flipped: movie.flipped }">
          <img :src="getImageUrl(movie.poster_path)" alt="Movie Poster" class="movie-poster" v-if="movie.poster_path" />
          <div class="movie-details">
            <strong class="movie-title">{{ movie.title }}</strong>
            <p>평점: {{ movie.vote_average }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</div>d
</template>

<script setup>
import axios from 'axios';
import router from '@/router';
import { ref, computed, onMounted } from 'vue';

const apiKey = '3691eda9c0d72053e1652d747c826899';
const moviesData = ref([]);

const movies = computed(() => {
  return moviesData.value.slice(0, 103);
});

async function fetchMovies(page) {
  const apiUrl = `https://api.themoviedb.org/3/discover/movie?sort_by=vote_average.desc&api_key=${apiKey}&language=ko-KR&page=${page}&vote_count.gte=500`;

  try {
    const response = await axios.get(apiUrl);
    const sortedMovies = response.data.results.sort((a, b) => b.vote_average - a.vote_average);
    moviesData.value = moviesData.value.concat(sortedMovies);

    if (moviesData.value.length < 103 && response.data.page < response.data.total_pages) {
      await fetchMovies(response.data.page + 1);
    } else {
      moviesData.value = moviesData.value.slice(0, 103);
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

onMounted(() => {
  fetchMovies(1);
});

const getImageUrl = (relativePath) => {
  if (relativePath) {
    return `https://image.tmdb.org/t/p/w500${relativePath}`;
  }
  return '';
};

const topTenMovies = computed(() => {
  return movies.value.slice(0, 10);
});

const otherMovies = computed(() => {
  return movies.value.slice(10);
});

const groupedOtherMovies = computed(() => {
  const groups = [];
  const remainingMovies = otherMovies.value.filter(movie => movie.poster_path);
  for (let i = 0; i < remainingMovies.length; i += 7) {
    groups.push(remainingMovies.slice(i, i + 7));
  }
  return groups;
});

const toggleFlip = (movie) => {
movie.flipped = !movie.flipped;
};

const goDetail = (movie) => {
  router.push(`/movies/${movie.id}`);
};

</script>

<style scoped>
.movie-info {
text-align: center;
}

.top-movie-poster {
width: 80%; /* 원하는 포스터 크기로 조절해주세요 */
height: auto;
display: inline-block; /* 포스터와 제목을 가로로 배치하기 위해 변경 */
vertical-align: middle; /* 제목과 포스터를 가운데 정렬하기 위해 추가 */
margin-bottom: 10px;
}

.movie-title {
display: block;
margin-bottom: 5px; /* 영화 제목 마진 조절 */
}

.movie-poster {
  width: 300%; /* 원하는 포스터 크기로 조절해주세요 */
  height: auto;
  display: block;
  margin: 2px;
}

.top-five, .other-five {
  display: inline-block;
  width: 20%;
  text-align: center;
  vertical-align: top;
  margin-bottom: 20px;
}

.nine-movies-per-line {
  list-style-type: none;
}

.seven-movies-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  padding: 0;
  margin: 0;
}

.other-movie-item {
width: calc(100% / 7 - 10px);
max-width: 150px;
height: auto;
text-align: center;
margin-bottom: 3px; /* 기본 마진 */
}

/* 큰 화면용 최대 마진 설정 */
@media (min-width: 1200px) {
.other-movie-item {
  margin-bottom: 2px;
}
}

/* 아주 큰 화면용 최대 마진 설정 */
@media (min-width: 1600px) {
.other-movie-item {
  margin-bottom: 1px;
}
}

.movie-title {
  display: block;
  text-align: center;
  margin-bottom: 5px; /* 영화 제목 마진 조절 */
}
/* 마우스 호버 시 포스터 회전 및 내용 표시 */
.movie-poster-container {
position: relative;
perspective: 1000px;
transition: transform 0.6s;
}

.movie-poster {
width: 100%;
height: auto;
display: block;
backface-visibility: hidden;
}

.movie-details {
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
backface-visibility: hidden;
transform: rotateY(180deg);
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
padding: 10px;
background-color: #fff;
transition: transform 0.6s;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
opacity: 0;
}

.movie-poster-container.flipped .movie-poster {
transform: rotateY(180deg);
}

.movie-poster-container:hover .movie-poster {
transform: rotateY(-180deg);
}

.movie-poster-container:hover .movie-details {
transform: rotateY(0);
opacity: 1;
}
</style>
