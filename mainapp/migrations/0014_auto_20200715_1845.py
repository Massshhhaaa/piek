# Generated by Django 3.0.5 on 2020-07-15 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20200715_1834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='firs_name',
            new_name='first_name',
        ),
    ]
