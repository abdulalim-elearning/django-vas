# Generated by Django 4.1.7 on 2023-03-22 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='height',
            field=models.FloatField(default=2),
        ),
    ]