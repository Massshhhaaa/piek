# Generated by Django 3.0.7 on 2020-08-06 21:30

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0067_auto_20200806_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mod_table',
            field=tinymce.models.HTMLField(help_text="Указание идентификатора обязательно. id = 'MOD'"),
        ),
    ]