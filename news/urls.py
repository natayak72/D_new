from django.contrib import admin
from django.urls import path
from .views import NewsList, NewsInstance

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>', NewsInstance.as_view(), name='news_item')
]