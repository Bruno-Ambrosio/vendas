# Generated by Django 4.2.6 on 2023-10-24 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_itens_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='numero',
            field=models.SmallIntegerField(),
        ),
    ]
