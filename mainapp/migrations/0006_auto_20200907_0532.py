# Generated by Django 3.0.7 on 2020-09-07 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20200907_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modification',
            name='meta_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='modification',
            name='meta_keywords',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
