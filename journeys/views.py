from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from journeys.models import Journey
from journeys.serializers import JourneySerializer


class JourneyViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    permission_classes = [AllowAny]
