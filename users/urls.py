from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = 'users'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('<username>/', views.ProfileView.as_view(), name='profile'),
    path('<username>/edit/', views.ProfileUpdateView.as_view(), name='edit'),
]
