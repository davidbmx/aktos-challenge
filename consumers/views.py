from rest_framework import viewsets, mixins

from consumers.models import Consumer
from consumers.serializers import ConsumerSerializer

class ConsumerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
    