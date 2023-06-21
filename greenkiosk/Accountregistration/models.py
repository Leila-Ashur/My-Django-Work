from django.db import models

# Create your models here.
class Register (models.Model):
   Firstname=models.CharField(max_length=32)
   Lastname=models.CharField(max_length=32)
   Password=models.CharField(max_length=15)
   Email=models.EmailField()
   Phone_number=models.CharField(max_length=10)


    
def __str__(self) :
    return self.name
