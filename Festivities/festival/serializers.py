from .models import Festivities, Location, Comment, Handicraft, Calender
from rest_framework import serializers
from django.contrib.auth.models import User

class FestivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festivities
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class HandicraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handicraft
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CalenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = '__all__'