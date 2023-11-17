from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    # path('recommended/', views.recommended, name='recommended'),
    path('<int:pk>/reviews/', views.reviews_create, name='reviews_create'),
    path('<int:movie_pk>/reviews/<int:comment_pk>/delete/', views.reviews_delete, name='reviews_delete'),
]
