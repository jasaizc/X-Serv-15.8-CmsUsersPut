from django.db import models

# Create your models here.
class Usuarios(models.Model):
    name = models.CharField(max_length = 32)
    birthday = models.CharField(max_length = 32)
