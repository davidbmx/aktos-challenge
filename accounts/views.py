from rest_framework import viewsets, mixins

from accounts.models import Account
from accounts.serializers import AccountSerializer, RequestParams

class AccountsView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def list(self, request):
        queryset = self.get_queryset()
        query_params = RequestParams(data=request.query_params)
        query_params.is_valid(raise_exception=True)
        validated_data = query_params.validated_data

        max_balance = validated_data.get('max_balance', None)
        min_balance = validated_data.get('min_balance', None)
        consumer_name = validated_data.get('consumer_name', None)
        status = validated_data.get('status', None)

        if max_balance:
            queryset = queryset.filter(balance__lte=max_balance)
        if min_balance:
            queryset = queryset.filter(balance__gte=min_balance)
        if consumer_name:
            queryset = queryset.filter(consumer__name__iexact=consumer_name)
        if status:
            queryset = queryset.filter(status=status)
        
        page = self.paginate_queryset(queryset=queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    
