# Generated by Django 3.2.7 on 2021-10-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='likes',
            field=models.IntegerField(default=0, max_length=11),
        ),
    ]