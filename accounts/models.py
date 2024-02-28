from django.db import models

from utils.model import AktosModel

class Account(AktosModel):
    client_reference_no = models.UUIDField()
    consumer = models.ForeignKey('consumers.Consumer', on_delete=models.CASCADE, related_name='balances')
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.consumer.name
    