from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import redirect
from .models import Location, Festivities, Comment, Handicraft, Calender
from .serializers import LocationSerializer, FestivitiesSerializer, CalenderSerializer, HandicraftSerializer, CommentSerializer
from django.http import JsonResponse
from django.db.models import Q, Prefetch
from datetime import date
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import logout


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
        # print(**kwargs)
        self.create(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
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
    
class CommentView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        else:
            data = self.list(request, *args, **kwargs).data
            for d in data:
                d['user'] = User.objects.get(id=d['user']).username
                # print(d['user'])
            # print(data)
            return JsonResponse(data,safe=False)
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    

class EventIdentifierView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FestivitiesSerializer

    def get(self, request, *args, **kwargs):
        name = request.GET.get('name') 
        dateparm = request.GET.get('date') 
        queryset = Festivities.objects.all()

        if name:
            queryset = queryset.filter(name__icontains=name)
        elif dateparm:
            queryset = queryset.filter(Q(start_date__lte=dateparm) & Q(end_date__gte=dateparm))
        else:
            queryset = queryset.filter(start_date__gte=date.today())

        if queryset.exists():
            top_10_results = list(queryset[:10].values()) 
            return JsonResponse(top_10_results, safe=False)
        else:
            return JsonResponse([], safe=False)

class HandicraftView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Handicraft.objects.all()
    serializer_class = HandicraftSerializer

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
    
    
class UserView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
    
class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        token = obtain_auth_token(request)
        return Response({'token': token.key})

class UserLogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=200)
    
class CalenderView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    
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
    