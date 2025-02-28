# Generated by Django 5.0.1 on 2024-02-04 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_playlist_song_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playlist_song",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.playlist_user"
            ),
        ),
        migrations.AlterField(
            model_name="playlist_user",
            name="username",
            field=models.CharField(max_length=200),
        ),
    ]
