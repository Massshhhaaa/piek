# Generated by Django 3.0.5 on 2020-08-11 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0072_auto_20200809_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modification',
            options={'ordering': ['parent__id']},
        ),
        migrations.AlterField(
            model_name='modification',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]