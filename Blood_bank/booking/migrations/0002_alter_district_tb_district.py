# Generated by Django 3.2.13 on 2022-05-18 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district_tb',
            name='district',
            field=models.CharField(blank=True, max_length=25, unique=True),
        ),
    ]
