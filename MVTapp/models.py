from django.db import models

# Create your models here.

class familia(models.Model):
    nombre= models.CharField(max_length=30)
    edad= models.IntegerField()
    fecha_de_nacimiento= models.DateField(null=True)