from django.urls import path
from .views import *


urlpatterns = [
   path('', PostsList.as_view(), name='posts'), 
   path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='search'),
   path('news/create/', CreatePost.as_view(), name='news_create'),
   path('articles/create/', CreatePost.as_view(), name='articles_create'),
   path('news/<int:pk>/update/', UpdatePost.as_view(), name='news_update'),
   path('articles/<int:pk>/update/', UpdatePost.as_view(), name='articles_update'),
   path('news/<int:pk>/delete/', DeletePost.as_view(), name='news_delete'),
   path('articles/<int:pk>/delete/', DeletePost.as_view(), name='articles_delete'),
]