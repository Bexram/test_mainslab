# Generated by Django 4.1.3 on 2022-11-24 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0002_alter_bill_clorgid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateField(),
        ),
    ]
