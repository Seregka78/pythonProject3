# Generated by Django 4.2.2 on 2024-03-06 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_disc',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_img_link',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_price',
        ),
    ]
