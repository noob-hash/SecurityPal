from .models import Festivities, Location
from rest_framework import serializers

class FestivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festivities
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'