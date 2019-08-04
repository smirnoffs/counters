# Generated by Django 2.2.4 on 2019-08-03 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0008_auto_20190803_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='value',
            name='address',
        ),
        migrations.RemoveField(
            model_name='value',
            name='owner',
        ),
        migrations.AddField(
            model_name='counter',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='readings.Address'),
        ),
    ]
