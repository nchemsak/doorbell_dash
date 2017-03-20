from django.contrib.auth.models import User
from rest_framework import serializers
from doorbell_dash_app.models import Photo, CachedImage
from doorbell_dash_app import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Photo
        fields = '__all__'


class CachedImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CachedImage
        fields = ('url', 'photo')
