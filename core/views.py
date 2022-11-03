from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProfileSerializer, OperationSerializer
from .models import Profile, Operations

@api_view(['GET'])
def Sample(request):
    queryset = Profile.objects.all().first()
    serializers = ProfileSerializer(queryset, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def SamplePost(request):
    p_name = Profile.objects.all().first()
    slack_name = p_name.slackUsername

    slackUsername = slack_name
    operation_type = request.POST['operation_type']
    x = request.POST['x']
    y = request.POST['y']

    if operation_type == 'addition':
        queryset1 = int(x) + int(y)
    elif operation_type == 'subtraction':
        queryset1 = int(x) - int(y)
    elif operation_type == 'multiplication':
        queryset1 = int(x) * int(y)
    queryset = OperationSerializer(data=request.data)

    if queryset.is_valid():
        return Response({
            'slackUsername': slack_name,
            'operation_type' : operation_type,
            'result': queryset1,
        })
    return Response(queryset.errors)