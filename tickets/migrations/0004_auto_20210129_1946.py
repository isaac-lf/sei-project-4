# Generated by Django 3.1.5 on 2021-01-29 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20210129_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='order',
            new_name='position',
        ),
    ]
