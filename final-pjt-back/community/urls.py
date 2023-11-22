from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('article_list_create/', views.article_list_create),
    path('detail/<int:article_pk>/', views.article_detail), 
    path('article/<int:article_pk>/', views.article_update_delete),
    path('article/create/', views.create_article),
    path('comments/<int:community_pk>', views.comment_list),
    path('<int:community_pk>/comment/', views.create_comment),
    path('comment/<int:community_pk>/<int:comment_pk>/', views.comment_delete_update),
]