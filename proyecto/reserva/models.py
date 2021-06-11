from django.db import models
from app.models import Profesor
# Create your models here.

class Clase(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    capacity=models.IntegerField()
    image=models.ImageField(upload_to="clases")
    image2=models.ImageField(upload_to="clases")
    reservas = models.ManyToManyField(Profesor, through='Reserv')
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Reserv(models.Model):
    id=models.AutoField(primary_key=True)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    reservationday=models.DateField()
    horainicio=models.DateTimeField(max_length=2)
    horafinal=models.DateTimeField(max_length=2)
    cantidad=models.IntegerField(blank=True, null=True)
    curso=models.CharField(max_length=6)
    motivo=models.CharField(max_length=150)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)

    unique_together = (("horainicio", "horafinal"),)

