# Generated by Django 5.0.4 on 2024-04-17 17:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0002_document_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='communication',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]