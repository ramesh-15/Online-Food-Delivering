# Generated by Django 4.1.5 on 2023-01-24 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_alter_user_address_alter_user_city_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="address",
        ),
        migrations.RemoveField(
            model_name="user",
            name="city",
        ),
        migrations.RemoveField(
            model_name="user",
            name="dd_email",
        ),
        migrations.RemoveField(
            model_name="user",
            name="dd_username",
        ),
        migrations.RemoveField(
            model_name="user",
            name="donation_from",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="user",
            name="pincode",
        ),
        migrations.RemoveField(
            model_name="user",
            name="state",
        ),
    ]