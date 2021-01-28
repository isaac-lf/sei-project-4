# Generated by Django 3.1.5 on 2021-01-28 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('complete', models.BooleanField(default=False)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tickets.ticket')),
            ],
        ),
    ]
