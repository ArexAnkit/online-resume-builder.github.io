# Generated by Django 3.2.4 on 2021-09-24 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_resume', '0013_auto_20210924_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='year_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='year_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='year_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]