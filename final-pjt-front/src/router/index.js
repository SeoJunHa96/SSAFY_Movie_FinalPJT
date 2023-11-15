import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/home/HomeView.vue'

import SignUpView from '@/views/accounts/SignUpView.vue'
import LoginView from '@/views/accounts/LoginView.vue'

import MyProfileView from '@/views/accounts/MyProfileView.vue'

import MovieView from '@/views/movie/MovieView.vue'
import MovieRankingView from '@/views/movie/MovieRankingView.vue'

import CommunityView from '@/views/community/CommunityView.vue'

import PlayView from '@/views/play/playView.vue'

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
      path: '/profile',
      name: 'MyProfileView',
      component: MyProfileView,
    },
    {
      path: '/movies',
      name: 'MovieView',
      component: MovieView,
    },
    {
      path: '/movieranking',
      name: 'MovieRanking',
      component: MovieRankingView,
    },
    {
      path: '/reviews',
      name: 'CommunityView',
      component: CommunityView
    },
    {
      path: '/play',
      name: 'PlayView',
      component: PlayView
    }
  ]
})

export default router
