# Generated by Django 5.0.3 on 2024-03-17 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_name_material_material_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='warehouse',
            old_name='material',
            new_name='material_w',
        ),
    ]