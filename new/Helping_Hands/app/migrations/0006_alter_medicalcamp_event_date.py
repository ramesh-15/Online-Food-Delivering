# Generated by Django 4.1.7 on 2023-05-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_animalcampmodel_bloodcamp_event_cbemodel_contact_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medicalcamp_event",
            name="Date",
            field=models.CharField(max_length=100),
        ),
    ]
