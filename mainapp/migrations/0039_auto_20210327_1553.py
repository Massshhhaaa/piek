# Generated by Django 3.1.7 on 2021-03-27 15:53

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0038_auto_20210124_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='img',
            new_name='icon',
        ),
        migrations.RemoveField(
            model_name='group',
            name='content',
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.CharField(blank=True, help_text='например stance, "mechanisms/meo"', max_length=200, null=True, unique=True, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=tinymce.models.HTMLField(help_text='Подзаголовки - H4. Черные подзаговолки просто как B'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.TextField(blank=True, help_text='Описание для поисковой системы (100-150символов)', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='mod_table',
            field=tinymce.models.HTMLField(help_text="Нужно идентификатора обязательно. id = 'MOD'"),
        ),
    ]
