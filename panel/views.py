from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from .models import panel
from .serializer import panelSerializer


# Create your views here.

class panelAPIView(generics.ListAPIView):
    queryset = panel.objects.all()
    serializer_class = panelSerializer
