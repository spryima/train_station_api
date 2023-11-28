from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from trains.models import Train, TrainType
from trains.serializers import TrainSerializer, TrainTypeSerializer


class TrainTypeViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = TrainType.objects.all()
    serializer_class = TrainTypeSerializer
    permission_classes = [AllowAny]


class TrainViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    permission_classes = [AllowAny]
