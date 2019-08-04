# Generated by Django 2.2.4 on 2019-08-03 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0006_auto_20190803_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='Значение:')),
                ('counter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readings.Counter')),
            ],
            options={
                'verbose_name': 'Показания',
                'verbose_name_plural': 'Показания',
            },
        ),
    ]
