<<<<<<< HEAD
# Generated by Django 3.1.1 on 2020-12-23 22:31
=======
# Generated by Django 3.1.4 on 2020-12-27 18:21
>>>>>>> 0273c3a2a869ef85f4c7a2249a77f9171f71fc0f

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0033_auto_20201223_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentation',
            name='document_category',
            field=models.CharField(choices=[('Общепром', 'Общепром'), ('Взрыв', 'Взрыв'), ('Датчики и контроллеры', 'Датчики и контроллеры'), ('Пусковые и управляющие', 'Пусковые и управляющие'), ('Шлагбаумы', 'Шлагбаумы')], max_length=255, null=True),
        ),
    ]
