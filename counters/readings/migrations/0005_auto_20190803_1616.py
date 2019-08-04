# Generated by Django 2.2.4 on 2019-08-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0004_auto_20190803_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30, verbose_name='Город, населенный пункт')),
                ('street', models.CharField(max_length=30, verbose_name='Улица')),
                ('house_number', models.IntegerField(blank=True, null=True, verbose_name='Номер дома')),
                ('hull_number', models.CharField(blank=True, max_length=5, verbose_name='Корпус')),
                ('apartment_number', models.IntegerField(blank=True, verbose_name='Квартира')),
            ],
            options={
                'verbose_name': 'Адреса',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.DeleteModel(
            name='Reading',
        ),
    ]
