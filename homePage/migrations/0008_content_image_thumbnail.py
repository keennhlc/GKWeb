# Generated by Django 2.2b1 on 2019-03-17 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0007_content_homecontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image_thumbnail',
            field=models.CharField(default='none', max_length=1000),
        ),
    ]
