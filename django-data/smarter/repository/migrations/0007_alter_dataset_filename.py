# Generated by Django 4.1.7 on 2023-03-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0006_dataset_dataset_datatype_owner_idx'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='filename',
            field=models.FilePathField(blank=True, max_length=255, null=True, path='/var/uwsgi/data', unique=True),
        ),
    ]
