# Generated by Django 2.2.2 on 2020-07-27 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='display_order',
            new_name='orders',
        ),
    ]
