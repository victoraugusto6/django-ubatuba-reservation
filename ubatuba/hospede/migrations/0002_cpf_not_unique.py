# Generated by Django 3.2.8 on 2021-10-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospede', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospede',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='CPF'),
        ),
    ]
