# Generated by Django 2.2.2 on 2020-07-27 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200727_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='create_time',
            new_name='created_time',
        ),
    ]
