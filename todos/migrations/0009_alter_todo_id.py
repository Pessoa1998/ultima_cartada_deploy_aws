# Generated by Django 5.0 on 2024-11-15 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0008_auto_20191202_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]