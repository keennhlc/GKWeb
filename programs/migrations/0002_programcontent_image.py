# Generated by Django 2.2b1 on 2019-03-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programcontent',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]