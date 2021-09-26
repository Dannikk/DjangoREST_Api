from django.db import models


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=60)
    desease = models.CharField(max_length=60)
    age = models.IntegerField()

    def __str__(self):
        return self.name
