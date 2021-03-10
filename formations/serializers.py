from rest_framework import serializers 
from .models import Formation, Game, Course
from users.models import User
#from users.serializers import UsersSerializer
from rest_framework.serializers import SerializerMethodField


class FormationSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, required=False)
    class Meta:
        model = Formation
        fields = "__all__"


class FormationRelatedField(serializers.RelatedField):
    def to_representation(self, instance):
        return FormationSerializer(instance).data

    def to_internal_value(self, data):
        return self.queryset.get(pk=data)


class GameSerializer(serializers.ModelSerializer):
    formation = FormationRelatedField(queryset=Formation.objects.all(), many=False)
    
    class Meta:
        model = Game
        fields = [
                    'name',
                    'formation'
                 ]


class CourseSerializer(serializers.ModelSerializer):
    formation = FormationRelatedField(queryset=Formation.objects.all(), many=False)

    class Meta:
        model = Course
        fields = [
                    'titre',
                    'types',
                    'formation'
                 ]