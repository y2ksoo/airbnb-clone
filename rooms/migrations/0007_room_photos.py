# Generated by Django 2.2.5 on 2020-07-03 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20200703_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='photos',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='rooms.Photo'),
        ),
    ]
