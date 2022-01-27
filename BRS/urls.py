from django.urls import path, include
from .views import views

urlpatterns = [
    path('homepage/', views.homepage),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    path('checkUser/', views.checkUser),
    path('search/', views.search)
]