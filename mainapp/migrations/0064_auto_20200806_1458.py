# Generated by Django 3.0.5 on 2020-08-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0063_auto_20200806_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modification',
            name='slug',
            field=models.SlugField(blank=True, help_text='заполняется автоматически от title', null=True, verbose_name='url'),
        ),
    ]