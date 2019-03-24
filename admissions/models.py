from django.db import models


class Admission(models.Model):
    title = models.CharField(max_length=250)
    steps = models.TextField(max_length=2500)
    image = models.CharField(max_length=1000)
    additional_info = models.TextField(max_length=10000)

    def __str__(self):
        return self.title
# Create your models here.
