from django.urls import path

from .views import (
    TeamListAPIView, PositionListAPIView, CollegeListAPIView,
    PlayerListCreateAPIView, PlayerRetrieveUpdateDestroyApiView
)

urlpatterns = [
    path('player/', PlayerListCreateAPIView.as_view(), name='player'),
    path('player/retrieve_update_destroy/<int:pk>',
         PlayerRetrieveUpdateDestroyApiView.as_view(), name='player_retrieve_update_destroy'),
    path('team/', TeamListAPIView.as_view(), name='team'),
    path('position/', PositionListAPIView.as_view(), name='position'),
    path('college/', CollegeListAPIView.as_view(), name='college')
]
