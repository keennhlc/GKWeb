# Generated by Django 2.2b1 on 2019-03-24 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_programcontent_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programcontent',
            name='image',
        ),
    ]
