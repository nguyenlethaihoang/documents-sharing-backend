# Generated by Django 4.1.2 on 2022-12-19 14:56

import course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_document_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=course.models.upload_path),
        ),
    ]
