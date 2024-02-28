from django.db import models

from utils.model import AktosModel

class Consumer(AktosModel):
    name = models.CharField(max_length=255)
    address = models.TextField()
    ssn = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.ssn}"
