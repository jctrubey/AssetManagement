from django.db import models

# Create your models here.

class Asset(models.Model):
    name = models.CharField(max_length=100)
    serialNumber = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    assignedUser = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    purhcasePrice = models.FloatField()

    def __str__(self):
        return self.name