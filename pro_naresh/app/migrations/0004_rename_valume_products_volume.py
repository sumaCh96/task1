# Generated by Django 4.1.3 on 2022-11-15 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_products_valume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='valume',
            new_name='volume',
        ),
    ]