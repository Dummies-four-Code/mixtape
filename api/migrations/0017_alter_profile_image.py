# Generated by Django 4.0.5 on 2022-06-28 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0016_alter_mixtape_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]
