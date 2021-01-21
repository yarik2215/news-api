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
    Return a paginated list of all news.

    retrieve:
    Return one news by id.

    create:
    Create new news instance.

    update:
    Update existing news by id.

    partial_update:
    Partial update existing news by id.

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
    list:
    Return a paginated list of comments for specified in url news.

    retrieve:
    Return one comment by id.

    create:
    Create new comment instance related to news specified in url.

    update:
    Update existing comment by id.

    partial_update:
    Partial update existing comment by id.

    destroy:
    Delete comment by id.
    """
    serializer_class = CommentSerializer

    def _get_news(self):
        """
        Get news id from url and return News instance with that id or 404.
        """
        news_id = self.kwargs.get("news_pk")
        return get_object_or_404(News, pk=news_id)

    def get_queryset(self):
        return Comment.objects.filter(news=self._get_news())

    def perform_create(self, serializer):
        serializer.save(news=self._get_news())
