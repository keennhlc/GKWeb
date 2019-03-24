from django.db import models


class HomeContent(models.Model):
    content_type = models.CharField(max_length=250)

# Create your models here.
    def __str__(self):
        return self.content_type + " - " + str(self.id)


class Content(models.Model):
    home_content = models.ForeignKey(HomeContent, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=10000)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/homePage', blank=True)
    image_thumbnail = models.ImageField(upload_to='images/homePage/thumbnail', blank=True)

    def __str__(self):
        return self.title + " - " + str(self.home_content) + " - " + str(self.id)
