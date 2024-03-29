# Generated by Django 2.2.4 on 2019-08-07 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0003_auto_20190803_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30, verbose_name='Город, населенный пункт')),
                ('street', models.CharField(max_length=30, verbose_name='Улица')),
                ('house_number', models.IntegerField(blank=True, null=True, verbose_name='Номер дома')),
                ('hull_number', models.CharField(blank=True, max_length=5, null=True, verbose_name='Корпус')),
                ('apartment_number', models.IntegerField(blank=True, null=True, verbose_name='Квартира')),
            ],
            options={
                'verbose_name': 'Адреса',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='CityOrVillage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_village', models.CharField(default=0, max_length=35, verbose_name='Место(Город, Село)')),
            ],
            options={
                'verbose_name': 'Город/Село',
                'verbose_name_plural': 'Город/Село',
            },
        ),
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=30, verbose_name='Отчество')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='readings.Address')),
            ],
            options={
                'verbose_name': 'Владелец',
                'verbose_name_plural': 'Владелец',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(verbose_name='Значение:')),
            ],
            options={
                'verbose_name': 'Показания',
                'verbose_name_plural': 'Показания',
            },
        ),
        migrations.AddField(
            model_name='counter',
            name='date_verification',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='counter',
            name='identifier',
            field=models.CharField(max_length=30, verbose_name='Id'),
        ),
        migrations.DeleteModel(
            name='Reading',
        ),
        migrations.AddField(
            model_name='value',
            name='counter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readings.Counter'),
        ),
        migrations.AddField(
            model_name='counter',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='readings.Address'),
        ),
        migrations.AddField(
            model_name='counter',
            name='city_or_village',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='readings.CityOrVillage'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='counter',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='readings.Owners'),
        ),
    ]
