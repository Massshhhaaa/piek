# Generated by Django 3.1 on 2020-08-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0081_auto_20200822_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdocs',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
