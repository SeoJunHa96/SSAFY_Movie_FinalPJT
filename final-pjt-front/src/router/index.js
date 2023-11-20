import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/home/HomeView.vue'

import SignUpView from '@/views/accounts/SignUpView.vue'
import LoginView from '@/views/accounts/LoginView.vue'

import MyProfileView from '@/views/accounts/MyProfileView.vue'

import MovieView from '@/views/movie/MovieView.vue'
import MovieRankView from '@/views/movie/MovieRankView.vue'
import MoviePopular from '@/components/movie/MoviePopular.vue'
import MovieVote from '@/components/movie/MovieVote.vue'

import CommunityView from '@/views/community/CommunityView.vue'
import CommunityDetailView from '@/views/community/CommunityDetailView.vue'

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
      path: '/play',
      name: 'PlayView',
      component: PlayView
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
    }

  ]
})

export default router
