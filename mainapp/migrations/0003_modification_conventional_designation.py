# Generated by Django 3.0.7 on 2020-08-27 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_modification_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='modification',
            name='conventional_designation',
            field=models.CharField(default='Fsf', max_length=250),
        ),
    ]
