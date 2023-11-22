import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/home/HomeView.vue'

import SignUpView from '@/views/accounts/SignUpView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import LogOutView from '@/views/accounts/LogOutView.vue'

import MyProfileView from '@/views/accounts/MyProfileView.vue'

import MovieView from '@/views/movie/MovieView.vue'
import MovieRankView from '@/views/movie/MovieRankView.vue'
import MoviePopular from '@/components/movie/MoviePopular.vue'
import MovieVote from '@/components/movie/MovieVote.vue'
import MoviePage from '@/views/movie/MoviePage.vue'
import MovieInfo from '@/components/InformConts.vue'

import CommunityView from '@/views/community/CommunityView.vue'
import CommunityDetailView from '@/views/community/CommunityDetailView.vue'
import CreateView from '@/views/community/CreateView.vue'

import MovieDetailView from '@/views/movie/MovieDetailView.vue'
import ActorView from '@/views/movie/ActorView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView,
    },
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView
    },
    {
      path: '/logOut',
      name: 'LogOutView',
      component: LogOutView
    },
    {
      path: '/profile',
      name: 'MyProfileView',
      component: MyProfileView,
    },
    {
      path: '/movieview',
      name: 'MovieView',
      component: MovieView,
    },
    {
      path: '/moviepage',
      name: 'Moviepage',
      component: MoviePage,
    },
    {
      path: '/inform',
      name: 'MovieInform',
      component: MovieInfo,
    },
    {
      path: '/movierank',
      name: 'MovieRank',
      component: MovieRankView,
    },
    {
      path: '/community',
      name: 'CommunityView',
      component: CommunityView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: CommunityDetailView
    },
    {
      path:'/movierank/populer',
      name: 'moviepopular',
      component: MoviePopular
    },
    {
      path:'/movierank/vote',
      name: 'movievote',
      component: MovieVote
    },
    {
      path:'/movies/:id',
      name: 'movieDetail',
      component: MovieDetailView
    },
    {
      path:'/actors/:id',
      name: 'actorView',
      component: ActorView
    },

  ]
})

import { useCounterStore } from '@/stores/counter'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'HomeView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }
  if ((to.name === 'HomeView' || to.name === 'LoginView') && (store.isLogin)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'ArticleView' }
  }
})

export default router
