# Generated by Django 3.0.7 on 2020-07-23 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_auto_20200723_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subgroupimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/mechanisms/'),
        ),
    ]