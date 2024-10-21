from rest_framework import serializers
from .models import Photo
from django.contrib.auth.models import User

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'filename', 'format', 'height', 'width', 'image', 'blur_data_url']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
