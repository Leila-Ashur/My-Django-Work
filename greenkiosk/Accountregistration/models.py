from django.db import models

# Create your models here.
class Accountregistration(models.Model):
   first_name=models.CharField(max_length=32)
   last_name=models.CharField(max_length=32)
   password=models.CharField(max_length=15)
   email=models.EmailField()
   phone_number=models.CharField(max_length=10)
    
def __str__(self) :
    return self.first_name
