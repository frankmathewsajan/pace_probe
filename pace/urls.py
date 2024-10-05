from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from space_apps import settings
from .views import views, auth

urlpatterns = [
    path('login/', auth.login, name='login'),
    path('register/', auth.register, name='register'),

    path('setup/', views.setup, name='setup'),
    path('courses/', views.courses, name='courses'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth.logout, name='logout'),

    path('', views.index, name='index'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
