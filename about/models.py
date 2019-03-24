from django.db import models


class AboutData(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='images/about', blank=True)

    def __str__(self):
        return self.title
