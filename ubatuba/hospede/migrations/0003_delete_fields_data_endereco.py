# Generated by Django 3.2.8 on 2021-10-05 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospede', '0002_cpf_not_unique'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospede',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='hospede',
            name='endereco',
        ),
    ]
