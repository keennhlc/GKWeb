# Generated by Django 2.2b1 on 2019-03-17 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactUs', '0002_contactinfo_middle_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='birthday',
            field=models.CharField(default='none', max_length=250),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='number',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='program',
            field=models.CharField(choices=[('BFA', 'BFA - Bachelor in Fine Arts'), ('BMMA', 'BMMA - Bachelor in Multimedia Arts'), ('BSIS', 'Bachelor of Science in Information System')], default='K12 Grad', max_length=1),
        ),
    ]
