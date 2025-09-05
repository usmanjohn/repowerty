from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list, name = 'profile-list'),
    path('register', views.profile_register, name = 'profile-register'),
    path('login', views.profile_login, name = 'profile-login'),
    path('logout', views.profile_logout, name = 'profile-logout'),
    path('update', views.profile_update, name = 'profile-update'),
    path('password-update', views.profile_password_update, name = 'profile-password-update'),
    path('profile/<str:username>/', views.profile_page, name='profile-page'),
]