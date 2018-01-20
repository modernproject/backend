from rest_framework import serializers
from project.posts.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class PostListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        exclude = ('content',)
