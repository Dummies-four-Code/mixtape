# Generated by Django 4.0.5 on 2022-06-24 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_remove_song_favorited_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="spotify_uri",
            field=models.TextField(default="", max_length=255),
        ),
    ]
