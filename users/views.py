from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import exceptions, viewsets, status
from .models import User, Permission, Role
from .serializers import UserSerializer
from .authentication import generate_token_access
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .authentication import JWTauthentication
from .serializers import PermissionSerializer, RoleSerializer
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


class RoleViewSet(viewsets.ViewSet):
    authentication_classes = [JWTauthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = RoleSerializer(Role.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(role)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = RoleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pl=None):
        role = Role.objects.get(id=pk)
        serializer = RoleSerializer(instance=role, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        role = Role.objects.get(id=pk)
        role.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
