# Generated by Django 4.1.7 on 2023-02-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_users_donations_donar_name_users_donations_message_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="users_donations",
            name="ngomessage",
            field=models.TextField(default="", max_length=300),
        ),
    ]