# Generated by Django 3.0.7 on 2020-07-02 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20200702_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hello',
            name='slug',
            field=models.SlugField(default=111, max_length=250, verbose_name='Url'),
            preserve_default=False,
        ),
    ]