# Generated by Django 2.2b1 on 2019-03-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campuses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campus',
            name='url',
            field=models.CharField(default='none', max_length=1000),
        ),
        migrations.AlterField(
            model_name='campus',
            name='email',
            field=models.CharField(max_length=500),
        ),
    ]
