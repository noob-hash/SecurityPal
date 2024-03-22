from .models import Festivities, Location, Comment
from rest_framework import serializers

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