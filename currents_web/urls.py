from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fy/', views.fy, name='fy'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('weather/', views.weather, name='weather'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('register/', views.register, name='register'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('about/', views.about, name='about'),
    path('change_password/',views.change_password, name='change_password'),
    path('set_favourite/',views.set_favourite, name='set_favourite'),
    path('favourites/',views.favourites, name='favourites'),
    path('metal_rates/', views.metal_rates, name="metal_rates"),
    path('subscription/', views.subscription, name='subscription'),

]
