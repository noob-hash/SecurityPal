from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import redirect
from .models import Location, Festivities
from .serializers import LocationSerializer, FestivitiesSerializer
from django.http import JsonResponse
# Create your views here.

class LocationView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class FestivitiesView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Festivities.objects.all()
    serializer_class = FestivitiesSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = Festivities.objects.all()
        search_param = self.request.query_params.get('q', None)
        if search_param:
            queryset = queryset.filter(name__icontains=search_param)
        return queryset

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class EventIdentifierView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        queryset = Festivities.objects.all()
        if queryset.exists():
            return redirect('festivities', pk=queryset.first().pk)
        else:
            return JsonResponse([], safe=False)