# Generated by Django 3.0.7 on 2020-10-07 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_remove_documentation_doc_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentation',
            options={'ordering': ['key_sort']},
        ),
        migrations.AddField(
            model_name='documentation',
            name='key_sort',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
