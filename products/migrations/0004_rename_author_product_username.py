# Generated by Django 5.0.4 on 2024-05-01 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='author',
            new_name='username',
        ),
    ]
