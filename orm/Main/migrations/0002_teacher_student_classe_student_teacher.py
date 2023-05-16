# Generated by Django 4.1.5 on 2023-05-16 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("prenom", models.CharField(max_length=150)),
                ("nom", models.CharField(max_length=150)),
                ("adresse", models.CharField(max_length=150)),
                ("telephone", models.CharField(max_length=150)),
                ("sexe", models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name="student",
            name="classe",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="teacher",
            field=models.CharField(default="", max_length=150, null=True),
        ),
    ]
