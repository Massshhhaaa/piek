# Generated by Django 3.0.7 on 2020-07-22 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20200721_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.URLField(null=True, unique=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='subgroupimage',
            name='image',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
