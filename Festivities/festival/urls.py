from django.urls import path,include
from .views import FestivitiesView, LocationView, EventIdentifierView

urlpatterns = [
    path('festivities/',FestivitiesView.as_view(),name='festivities'),
    path('festivities/<int:pk>/',FestivitiesView.as_view(),name='festivities'),
    path('locations/',LocationView.as_view(),name='locations'),
    path('locations/<int:pk>/',LocationView.as_view(),name='locations'),
    path('find_festivities/',EventIdentifierView.as_view(),name='find-festvities'),
]
