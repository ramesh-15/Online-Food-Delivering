# Generated by Django 4.1.5 on 2023-01-25 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0006_users_donations"),
    ]

    operations = [
        migrations.RenameField(
            model_name="users_donations",
            old_name="ud_username",
            new_name="food_name",
        ),
        migrations.RemoveField(
            model_name="users_donations",
            name="donation",
        ),
        migrations.RemoveField(
            model_name="users_donations",
            name="food_items",
        ),
    ]