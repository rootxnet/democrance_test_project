from django.db import models

from contrib.models import BaseModel


class Customer(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
