# Generated by Django 4.1 on 2023-04-26 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_post_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
