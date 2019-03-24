from django.db import models


class Program(models.Model):
    program_name = models.CharField(max_length=250)
    program_image = models.ImageField(upload_to='images/programs', blank=True)

    def __str__(self):
        return self.program_name


class ProgramContent(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    content = models.TextField(max_length=10000)
    content_image = models.ImageField(upload_to='images/programs/content', blank=True)

    def __str__(self):
        return str(self.program)



