# Generated by Django 2.2b1 on 2019-03-11 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0003_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slidercontent',
            name='slider',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
        migrations.DeleteModel(
            name='SliderContent',
        ),
    ]
