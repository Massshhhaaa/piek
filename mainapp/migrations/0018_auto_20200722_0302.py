# Generated by Django 3.0.7 on 2020-07-22 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20200722_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='url'),
        ),
    ]
