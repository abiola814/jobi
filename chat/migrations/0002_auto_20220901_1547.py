# Generated by Django 3.0 on 2022-09-01 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='time_stamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
