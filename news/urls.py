from django.contrib import admin
from django.urls import path
from .views import NewsList, NewsInstance, NewsCreate

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>', NewsInstance.as_view(), name='news_item')
]