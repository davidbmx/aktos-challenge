from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from consumers.models import Consumer
from consumers.serializers import ConsumerSerializer
from utils.file_handler import ingest_data

class ConsumerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer

    @action(detail=False, methods=['POST'], parser_classes=[MultiPartParser], url_path='upload-balances')
    def upload_balances(self, request):
        csv_data = request.FILES.get('csv_data', None)
        if csv_data:
            ingest_data(csv_data=csv_data)

        return Response({'success': True}, status=status.HTTP_201_CREATED)
    