# Generated by Django 4.0.2 on 2022-02-23 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_promotions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='promotions',
        ),
        migrations.DeleteModel(
            name='Promotion',
        ),
    ]
