# Generated by Django 3.0.7 on 2020-07-29 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0035_auto_20200729_1245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='slug',
            new_name='slug_product',
        ),
    ]