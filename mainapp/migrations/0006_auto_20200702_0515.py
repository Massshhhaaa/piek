# Generated by Django 3.0.7 on 2020-07-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20200702_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='slug',
            field=models.SlugField(max_length=250, unique=True, verbose_name='url'),
        ),
    ]
