from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProfileSerializer
from .models import Profile

@api_view(['GET'])
def Sample(request):
    queryset = Profile.objects.all().first()
    serializers = ProfileSerializer(queryset, many=False)
    return Response(serializers.data)