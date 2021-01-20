from rest_framework.generics import get_object_or_404
from .models import News, Comment
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import (
    NewsSerializer,
    CommentSerializer,
)


class NewsViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all news.

    retrieve:
    Return one news by id,
    with related comments.

    create:
    Create new news instance.

    update:
    Update existing news by id.

    destroy:
    Delete news by id.

    upvote:
    Upvote for current news.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    paginate_by = 10

    @action(detail=True)
    def upvote(self, request, *args, **kwargs):
        self.get_object().upvote()
        return Response(status=200)


class CommentsViewSet(viewsets.ModelViewSet):
    """
    """
    serializer_class = CommentSerializer

    def _get_news(self):
        news_id = self.kwargs.get("news_pk")
        return get_object_or_404(News, pk=news_id)

    def get_queryset(self):
        return Comment.objects.filter(news=self._get_news())

    def perform_create(self, serializer):
        serializer.save(news=self._get_news())
