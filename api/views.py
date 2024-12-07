from django.shortcuts import render
from rest_framework import generics
from app.api.models import BlogPost
from app.api.serializers import BlogPostSerializer

# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    