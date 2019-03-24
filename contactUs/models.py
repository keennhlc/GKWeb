from django.db import models
from django.contrib.auth.models import User


class ContactInfo(models.Model):
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    birthday = models.CharField(max_length=250)
    email = models.EmailField()
    contact_number = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    PROGRAM_CHOICES = (
        ('BFA', 'BFA - Bachelor in Fine Arts'),
        ('BMMA', 'BMMA - Bachelor in Multimedia Arts'),
        ('BSIS', 'Bachelor of Science in Information System'),
    )
    interested_course = models.CharField(max_length=4, choices=PROGRAM_CHOICES, default='BFA')
    SCHOOL_CHOICES = (
        ('K12 Grad', 'K12 Graduate'),
        ('College Trans', 'College Transferee'),
        ('College Grad', 'College Graduate'),
    )
    previous_schooling = models.CharField(max_length=13, choices=SCHOOL_CHOICES, default='K12 Grad')

    def __str__(self):
        return self.interested_course + " - " + str(self.id)
# Create your models here.
