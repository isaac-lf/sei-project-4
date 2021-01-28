# Generated by Django 3.1.5 on 2021-01-27 16:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20210127_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]