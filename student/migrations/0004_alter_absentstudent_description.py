# Generated by Django 3.2.5 on 2021-10-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20211025_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absentstudent',
            name='description',
            field=models.TextField(blank=True, default=' '),
        ),
    ]