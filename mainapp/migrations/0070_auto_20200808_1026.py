# Generated by Django 3.0.7 on 2020-08-08 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0069_modification_h1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modification',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]