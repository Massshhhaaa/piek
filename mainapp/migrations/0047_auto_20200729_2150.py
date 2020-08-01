# Generated by Django 3.0.5 on 2020-07-29 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0046_auto_20200729_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='href_title',
            field=models.CharField(default=1, max_length=250, verbose_name='Имя ссылки'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(null=True, upload_to='mechanisms_preview', verbose_name='Изображение для ссылки'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Имя группы'),
        ),
    ]