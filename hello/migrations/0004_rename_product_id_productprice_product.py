# Generated by Django 5.0.3 on 2024-03-19 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_productprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productprice',
            old_name='product_id',
            new_name='product',
        ),
    ]
