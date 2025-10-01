
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import SpyCat, Mission, Target, Breed
from .permisions import IsAdminOrIfAuthenticatedReadOnly
from .serializers import (
    SpyCatSerializer,
    SpyCatUpdateSerializer,
    MissionSerializer,
    MissionCreateSerializer,
    TargetSerializer,
    TargetUpdateSerializer, BreedSerializer, SpyCatListSerializer, TargetCreateSerializer, MissionListSerializer,
    MissionDetailSerialize, MissionUpdateSerializer, TargetListSerializer, MissionAssignCatSerializer,
    MissionUniqueTargetSerializer
)

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all().select_related("breed")
    serializer_class = SpyCatSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        if self.action == 'partial_update' or self.action == 'update':
            return SpyCatUpdateSerializer
        if self.action =='list':
            return SpyCatListSerializer
        return SpyCatSerializer

class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        if self.action == 'create':
            return TargetCreateSerializer
        if self.action == 'update' or 'partial_update':
            return TargetUpdateSerializer
        if self.action == 'list':
            return TargetListSerializer
        return TargetSerializer


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all().select_related('cat', 'target')
    serializer_class = MissionSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_serializer_class(self):
        if self.action == 'list':
            return MissionListSerializer
        if self.action == 'retrieve':
            return MissionDetailSerialize
        if self.action == 'partial_update':
            return MissionUpdateSerializer
        if self.action == 'create':
            return MissionCreateSerializer
        return MissionSerializer

    @action(detail=True, methods=['post'])
    def assign_cat(self, request, pk=None):
        mission = self.get_object()
    
        if mission.cat is not None:
            return Response(
                {"error": "Mission already has a cat assigned"},
                status=status.HTTP_400_BAD_REQUEST
            )
    
        serializer = MissionAssignCatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        cat = SpyCat.objects.get(id=serializer.validated_data['cat_id'])
        mission.cat = cat
        mission.save()
    
        return Response(MissionSerializer(mission).data)
    

    @action(detail=True, methods=['post'])
    def check_targets(self, request, pk=None):
        mission = self.get_object()
    
        if mission.target is not None:
            return Response(
                {"error": "Target already has a mission assigned"},
                status=status.HTTP_400_BAD_REQUEST
            )
    
        serializer = MissionUniqueTargetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        target = Target.objects.get(id=serializer.validated_data['target_id'])
        mission.target = target
        mission.save()
    
        return Response(MissionSerializer(mission).data)
