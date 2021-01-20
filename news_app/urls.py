from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

news_router = DefaultRouter()
news_router.register(r'news', views.NewsViewSet, basename='news')
comment_router = DefaultRouter()
comment_router.register(r'comments', views.CommentsViewSet, basename='comments')

urlpatterns = [
    path('', include(news_router.urls)),
    path('news/<int:news_pk>/', include(comment_router.urls))
]
