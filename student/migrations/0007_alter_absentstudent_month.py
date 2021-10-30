# Generated by Django 3.2.5 on 2021-10-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_absentstudent_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absentstudent',
            name='month',
            field=models.CharField(choices=[('مهر', 'مهر'), ('aban', 'آبان'), ('azar', 'آذر'), ('daye', 'دی'), ('bahman', 'بهمن'), ('esfand', 'اسفند'), ('farvardin', 'فروردین'), ('ordibehesht', 'اردیبهشت'), ('khordad', 'خرداد'), ('tir', 'تیر'), ('mordad', 'مرداد'), ('shahrivar', 'شهریور')], default='mehr', max_length=15),
        ),
    ]