from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

app_name = 'accounts'

urlpatterns = [
    path('users/', views.users),
    path('user/<int:my_pk>/', views.user),
    path('signup/', views.signup),
    path('logout/', views.logout),
    path('login/', views.custom_login),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('myprofile/', views.my_profile),
    path('follow/<int:my_pk>/<int:user_pk>/', views.follow),
    path('is_follow/<int:my_pk>/<int:user_pk>/', views.is_follow),
    path('info/', views.users_info),
    path('profile/<int:id>/', views.get_my_profile),
]
