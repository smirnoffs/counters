# Generated by Django 2.2.4 on 2019-08-07 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0004_auto_20190807_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faza', models.CharField(default=0, max_length=35, verbose_name='Количество фаз')),
            ],
            options={
                'verbose_name': 'Однофазный/Трёхфазный',
                'verbose_name_plural': 'Однофазный/Трёхфазный',
            },
        ),
        migrations.AlterField(
            model_name='counter',
            name='city_or_village',
            field=models.ForeignKey(on_delete='DO_NOTHING', to='readings.CityOrVillage'),
        ),
        migrations.AddField(
            model_name='counter',
            name='faza',
            field=models.ForeignKey(default=1, on_delete='DO_NOTHING', to='readings.Faza'),
            preserve_default=False,
        ),
    ]