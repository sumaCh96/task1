# Generated by Django 4.1.3 on 2022-11-15 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='stock_qty',
            field=models.IntegerField(),
        ),
    ]
