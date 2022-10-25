# Generated by Django 4.1.2 on 2022-10-24 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.IntegerField(max_length=10000, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=10)),
                ('subjectID', models.CharField(max_length=100)),
                ('userID', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.IntegerField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('majorID', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(max_length=255, primary_key=True, serialize=False)),
                ('studentID', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('permisson', models.IntegerField(default=1, max_length=3)),
            ],
        ),
    ]
