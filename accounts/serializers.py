from rest_framework import serializers

from accounts.models import Account
from consumers.serializers import ConsumerSerializer

class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for accounts and nested consumer serializer
    """
    consumer = ConsumerSerializer(many=False)
    class Meta:
        model = Account
        fields = '__all__'

class RequestParams(serializers.Serializer):
    """
    Serializer for validate query params request
    """
    min_balance = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    max_balance = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    consumer_name = serializers.CharField(required=False)
    status = serializers.CharField(required=False)