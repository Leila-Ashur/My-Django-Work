# Generated by Django 4.2.3 on 2023-07-16 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0003_rename_shopping_shoppingcart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='Product',
            new_name='product',
        ),
    ]
