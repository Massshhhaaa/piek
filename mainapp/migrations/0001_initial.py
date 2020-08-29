# Generated by Django 3.1 on 2020-08-27 12:16

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('position', models.IntegerField(unique=True, verbose_name='Позиция на странице')),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Название на странице группы')),
                ('img', models.ImageField(blank=True, null=True, upload_to='main_page')),
                ('slug', models.CharField(blank=True, help_text='for instance, "mechanisms/meo"', max_length=200, null=True, unique=True, verbose_name='url')),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('pic_of_hat', models.ImageField(blank=True, help_text='size: 1920x500px', null=True, upload_to='pic_of_hat')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_product', models.SlugField(help_text='for instance, "40 or 6_3"', verbose_name='url')),
                ('img', models.ImageField(blank=True, null=True, upload_to='mechanisms_preview', verbose_name='Изображение для ссылки')),
                ('href_title', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('h1_mod', models.CharField(max_length=250)),
                ('mod_table', tinymce.models.HTMLField(help_text="Указание идентификатора обязательно. id = 'MOD'")),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('content', tinymce.models.HTMLField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.group')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='mechanisms')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(upload_to='')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Modification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug_mod', models.SlugField(blank=True, help_text='заполняется автоматически от title', null=True, verbose_name='url')),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
            options={
                'ordering': ['parent__id'],
            },
        ),
    ]