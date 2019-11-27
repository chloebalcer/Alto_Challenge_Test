from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ChallengeSerializer
from .models import Challenge


class ChallengeView(viewsets.ModelViewSet):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()
