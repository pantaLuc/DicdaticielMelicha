from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import exceptions
from .models import User, Permission
from .serializers import UserSerializer
from .authentication import generate_token_access
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .authentication import JWTauthentication
from .serializers import PermissionSerializer
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

# signin function


@api_view(['POST'])
def signin(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = User.objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not Found')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('incorrect password')

    response = Response()
    token = generate_token_access(user)
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response


# current_user do it with class APIView

class CurrentUser(APIView):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({
            'data': serializer.data
        })

# logout function


@api_view(['POST'])
def signout(request):
    response = Response()
    response.delete_cookie(key='jwt')
    response.data = {
        'message': 'succes'
    }
    return response


@api_view(['GET'])
def users(request):
    serializer = UserSerializer(User.objects.all(), many=True)

    return Response(serializer.data)


class PermissionView(APIView):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PermissionSerializer(Permission.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })
