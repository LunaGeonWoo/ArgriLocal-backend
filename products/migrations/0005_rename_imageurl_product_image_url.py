# Generated by Django 5.0.6 on 2024-07-05 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='imageUrl',
            new_name='image_url',
        ),
    ]
