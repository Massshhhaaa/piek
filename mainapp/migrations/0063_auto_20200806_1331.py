# Generated by Django 3.0.5 on 2020-08-06 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0062_auto_20200806_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modification',
            old_name='titile',
            new_name='title',
        ),
    ]
