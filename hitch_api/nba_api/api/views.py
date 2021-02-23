from .base_views import GeneralListApiView
from rest_framework import generics
from .serializers import (
    PlayerSerializer, TeamSerializer, PositionSerializer,
    CollegeSerializer
)


class PlayerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self, pk=None):
        return self.get_serializer().Meta.model.objects.all()


class PlayerRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self, pk=None):
        return self.get_serializer().Meta.model.objects.all()


class TeamListAPIView(GeneralListApiView):
    serializer_class = TeamSerializer


class PositionListAPIView(GeneralListApiView):
    serializer_class = PositionSerializer


class CollegeListAPIView(GeneralListApiView):
    serializer_class = CollegeSerializer
