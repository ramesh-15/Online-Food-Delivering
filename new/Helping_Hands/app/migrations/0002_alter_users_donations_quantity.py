# Generated by Django 4.1.7 on 2023-04-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users_donations",
            name="quantity",
            field=models.CharField(default="0", max_length=100),
        ),
    ]