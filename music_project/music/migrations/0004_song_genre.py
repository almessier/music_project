# Generated by Django 3.2.7 on 2021-10-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_song_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(default='song', max_length=50),
            preserve_default=False,
        ),
    ]