# Generated by Django 3.2.4 on 2021-09-03 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_resume', '0006_auto_20210903_0025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='address',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='person',
            name='occupation',
            field=models.TextField(),
        ),
    ]