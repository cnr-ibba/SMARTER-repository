# Generated by Django 4.1.7 on 2023-02-21 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_alter_dataset_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='embargo',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
