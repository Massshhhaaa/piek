# Generated by Django 3.0.7 on 2020-11-28 11:20

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_auto_20201128_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sensors',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('М', 'М'), ('У', 'У'), ('Р', 'Р'), ('И', 'И'), ('БЦА', 'БЦА')], max_length=10, null=True),
        ),
    ]