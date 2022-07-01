from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

