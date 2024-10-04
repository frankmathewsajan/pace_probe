from django.urls import path

from .views import views, auth

urlpatterns = [
    path('login', auth.login, name='login'),
    path('register', auth.register, name='register'),

    path('setup', views.setup, name='setup'),
path('profile', views.profile, name='profile'),
    path('logout', auth.logout, name='logout'),

    path('', views.index, name='index'),

]
