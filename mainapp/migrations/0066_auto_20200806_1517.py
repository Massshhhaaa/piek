# Generated by Django 3.0.5 on 2020-08-06 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0065_auto_20200806_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modification',
            old_name='slug',
            new_name='slug_mod',
        ),
    ]