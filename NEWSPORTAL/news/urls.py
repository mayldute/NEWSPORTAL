from django.urls import path
from .views import *


urlpatterns = [
   path('', PostsList.as_view(), name = 'posts'), 
   path('<int:pk>/', PostDetail.as_view(), name = 'post_detail'),
   path('search/', PostSearch.as_view()),
   path('news/create/', CreatePost.as_view()),
   path('articles/create/', CreatePost.as_view()),
   path('news/<int:pk>/update/', UpdatePost.as_view()),
   path('articles/<int:pk>/update/', UpdatePost.as_view()),
   path('news/<int:pk>/delete/', DeletePost.as_view()),
   path('articles/<int:pk>/delete/', DeletePost.as_view()),
]
