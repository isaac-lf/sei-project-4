# Generated by Django 3.1.5 on 2021-01-27 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kanbans', '0002_auto_20210127_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('position', models.PositiveIntegerField()),
                ('kanban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='kanbans.kanban')),
            ],
        ),
    ]