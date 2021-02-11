from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import exceptions
from .models import User
from .serializers import UserSerializer
# Create your views here.


@api_view(['POST'])
def signup(request):
    data = request.data
    if data['password'] != data['password_confirm']:
        raise exceptions.APIException(
            "les mots de passes ne correspondent pas")
    serializer = UserSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def users(request):
    serializer = UserSerializer(User.objects.all(), many=True)
    return Response(serializer.data)
