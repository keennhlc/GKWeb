from django.db import models


class Campus(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    contact_info = models.CharField(max_length=250)
    opening = models.TimeField()
    closing = models.TimeField()
    open_days = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/campuses', blank=True)
    info = models.TextField(max_length=20000)
    url = models.CharField(max_length=1000, default='none')

    def __str__(self):
        return self.name
