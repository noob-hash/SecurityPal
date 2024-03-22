from django.urls import path,include
from .views import FestivitiesView, CalenderView, UserLoginAPIView, LocationView, HandicraftView, EventIdentifierView, CommentView, UserLogoutAPIView, UserView

urlpatterns = [
    path('festivities/',FestivitiesView.as_view(),name='festivities'),
    path('festivities/<int:pk>/',FestivitiesView.as_view(),name='festivities'),
    path('locations/',LocationView.as_view(),name='locations'),
    path('locations/<int:pk>/',LocationView.as_view(),name='locations'),
    path('find_festivities/',EventIdentifierView.as_view(),name='find-festvities'),
    path('comments/',CommentView.as_view(),name='comments'),
    path('comments/<int:pk>/',CommentView.as_view(),name='comments'),
    path('handicrafts/',HandicraftView.as_view(),name='handicrafts'),
    path('handicrafts/<int:pk>/',HandicraftView.as_view(),name='handicrafts'),
    path('calender/',CalenderView.as_view(),name='calender'),
    path('calender/<int:pk>',CalenderView.as_view(), name='calender'),
    path('users/', UserView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserView.as_view(), name='users-detail'),
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    path('logout/', UserLogoutAPIView.as_view(), name='user_logout'),
]
