# Generated by Django 4.1.2 on 2022-11-15 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('cost_per_item', models.FloatField()),
                ('stock_quantity', models.IntegerField()),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
