# Generated by Django 3.0.7 on 2020-07-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0050_auto_20200730_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subgroup',
            name='name',
        ),
        migrations.AddField(
            model_name='categories',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]