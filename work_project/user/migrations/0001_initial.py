# Generated by Django 4.2.1 on 2023-06-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [()]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                ("email", models.EmailField(max_length=30)),
                ("description", models.TextField(max_length=300)),
                ("active", models.BooleanField(default=True)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=6
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
