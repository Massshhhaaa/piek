# Generated by Django 3.0.7 on 2020-09-17 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_productdocs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_group', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='productdocs',
            name='file',
        ),
        migrations.RemoveField(
            model_name='productdocs',
            name='name',
        ),
        migrations.AddField(
            model_name='productdocs',
            name='item',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Documentation'),
            preserve_default=False,
        ),
    ]
