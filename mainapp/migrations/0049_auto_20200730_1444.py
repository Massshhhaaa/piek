# Generated by Django 3.0.7 on 2020-07-30 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0048_auto_20200729_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='name',
            new_name='title',
        ),
    ]