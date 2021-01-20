from rest_framework import serializers
from .models import News, Comment


class CommentSerializer(serializers.ModelSerializer):
    news = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    upvotes = serializers.ReadOnlyField()

    class Meta:
        model = News
        fields = '__all__'
