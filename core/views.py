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
    p_name = Profile.objects.get(id=1)
    slack_name = p_name.slackUsername

    slackUsername = slack_name
    operation_type = request.data.get("operation_type")
    x = request.data.get('x')
    y = request.data.get('y')

    if operation_type == 'addition':
        queryset1 = int(x) + int(y)
    elif operation_type == 'subtraction':
        queryset1 = int(x) - int(y)
    elif operation_type == 'multiplication':
        queryset1 = int(x) * int(y)
    
    queryset = OperationSerializer(data=request.data)

    if queryset.is_valid():
        queryset.save()
        return Response({
            'slackUsername': slack_name,
            'result': queryset1,
            'operation_type' : request.data['operation_type'],
        })
    return Response(queryset.errors)
    