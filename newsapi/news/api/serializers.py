from datetime import datetime

from django.utils.timesince import timesince
from rest_framework import serializers
from ..models import Article, Journalist


# serializers based on models
class ArticleSerializer(serializers.ModelSerializer):
    # creating new field
    time_since_publication = serializers.SerializerMethodField()
    # author = serializers.StringRelatedField()
    # author = JournalistSerializer()

    class Meta:
        model = Article
        exclude = ("id",)
        # fields = "__all__"  # we want all the fields of our model
        # fields = ("title", "description", 'body')  # we want the following fields

    def get_time_since_publication(self, object):
        pulication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(pulication_date, now)
        return time_delta

    # object level validation of serializers
    def validate(self, data):
        """check that description & title are different
           https://www.django-rest-framework.org/api-guide/serializers/"""
        if data["title"] == data["description"]:
            raise serializers.ValidationError("Title & Description must be different to one another")
        return data

    # field level validation of serializers
    def validate_title(self, value):
        """check that title has at least 30 characters"""
        if len(value) < 30:
            raise serializers.ValidationError("Title should be 30 characters long at least")
        return value


class JournalistSerializer(serializers.ModelSerializer):
    # article = ArticleSerializer(many=True, read_only=True)
    articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article-detail")

    class Meta:
        model = Journalist
        fields = "__all__"

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     description = serializers.CharField()
#     body = serializers.CharField()
#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#     def create(self, validated_data):
#         print(validated_data)
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     # object level validation
#     def validate(self, data):
#         """check that description & title are different"""
#         if data["title"] == data["description"]:
#             raise serializers.ValidationError("Title & Description must be different to one another")
#         return data
#
#     # field level validation
#     def validate_title(self, value):
#         if len(value) < 30:
#             raise serializers.ValidationError("Title should be 30 characters long at least")
#         return value
