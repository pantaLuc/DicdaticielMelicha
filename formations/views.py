from django.db.models import Q
import datetime
from django.shortcuts import render
from .models import Formation, Game, Course
from rest_framework.response import Response
from django.core.files.storage import default_storage
from rest_framework.parsers import MultiPartParser, JSONParser
from .serializers import FormationSerializer, GameSerializer, CourseSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import exceptions, status, generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
# from users.authentication import JwtAuthenticatedUser
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.core.exceptions import ObjectDoesNotExist


class FormationViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = FormationSerializer(Formation.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        formation = Formation.objects.get(id=pk)
        serializer = FormationSerializer(formation)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = FormationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        formation = Formation.objects.get(id=pk)
        serializer = FormationSerializer(instance=formation, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        formation = Formation.objects.get(id=pk)
        formation.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class GameViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = GameSerializer(Game.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        game = Game.objects.get(id=pk)
        serializer = GameSerializer(game)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = GameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        game = Game.objects.get(id=pk)
        serializer = GameSerializer(instance=game, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        game = Game.objects.get(id=pk)
        game.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class CourseViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = CourseSerializer(Course.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        course = Course.objects.get(id=pk)
        serializer = CourseSerializer(course)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        course = Course.objects.get(id=pk)
        serializer = CourseSerializer(instance=course, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        course = Course.objects.get(id=pk)
        course.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class FileUploadView(APIView):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]
    parser_classes = (JSONParser, )

    def post(self, request):
        file = request.FILES['image']
        file_name = default_storage.save(file.name, file)
        url = default_storage.url(file_name)

        return Response({
            'url': url
        })

