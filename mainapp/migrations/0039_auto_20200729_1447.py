# Generated by Django 3.0.7 on 2020-07-29 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0038_auto_20200729_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='parental_slug',
            new_name='parent',
        ),
    ]