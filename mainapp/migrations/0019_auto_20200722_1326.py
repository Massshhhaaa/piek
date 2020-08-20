# Generated by Django 3.0.7 on 2020-07-22 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_auto_20200722_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.CharField(help_text='for instance, "catalog/mechanisms/meo"', max_length=200, null=True, unique=True, verbose_name='url'),
        ),
    ]
