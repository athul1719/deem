# Generated by Django 4.2.7 on 2023-12-08 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0002_rename_cart_id_cart_cartid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cartid',
            new_name='cart_id',
        ),
        migrations.RenameField(
            model_name='cartitem',
            old_name='cart',
            new_name='Cart',
        ),
    ]
