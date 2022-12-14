# Generated by Django 4.1.2 on 2022-10-27 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("slackUsername", models.CharField(max_length=200)),
                ("backend", models.BooleanField(default=False)),
                ("age", models.IntegerField()),
                ("bio", models.CharField(max_length=1000)),
            ],
        ),
    ]
