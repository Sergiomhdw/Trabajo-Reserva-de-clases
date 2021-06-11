from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profesor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    image=models.ImageField(upload_to="profesores")
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    
    def __str__(self):
        return self.name



