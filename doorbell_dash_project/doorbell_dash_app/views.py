from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import viewsets, generics
from doorbell_dash_app import serializers, models
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer


class CachedImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows photos to be viewed or edited.
    """
    queryset = models.CachedImage.objects.all()
    serializer_class = serializers.CachedImageSerializer


# @api_view(['GET'])
# def get_pic(request, pk=None, format=None):
#     # //get image and mimetype here
#     return HttpResponse(image, content_type=mimetype)


# class JPEGRenderer(APIView):
#     media_type = 'image/jpeg'
#     format = 'jpg'
#     charset = None
#     render_style = 'binary'

#     def render(self, data, media_type=None, renderer_context=None):
#         return data
