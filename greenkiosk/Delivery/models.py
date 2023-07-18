from django.db import models


# Create your models here.
class Delivery(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    is_delivered = models.BooleanField(default=False)

