# Generated by Django 2.2.4 on 2019-08-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0009_auto_20190807_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='subsidy',
            field=models.CharField(choices=[('Нету', 'Нету'), ('Есть', 'Есть')], default='Нету', max_length=30, verbose_name='Субсидия'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='city_or_village',
            field=models.CharField(choices=[('Город', 'Город'), ('Село', 'Село')], default='Город', max_length=10, verbose_name='Город или село'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='faza',
            field=models.CharField(choices=[('Однофазный', 'Однофазный'), ('Трёхфазный', 'Трёхфазный')], default='Однофазный', max_length=10, verbose_name='Количество фаз'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='rate',
            field=models.CharField(choices=[('1', 'Тариф 1'), ('2', 'Тариф 2'), ('3', 'Тариф 3')], default='1', max_length=10, verbose_name='Тариф'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='region',
            field=models.CharField(choices=[('Херсонская область', 'Херсонская область'), ('Николаевская область', 'Николаевская область'), ('Запорожская область', 'Запорожская область')], default='Херсонская область', max_length=30, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='subscriber',
            field=models.CharField(choices=[('Население', 'Население'), ('Железнодорожный', 'Железнодорожный'), ('Юридический', 'Юридический'), ('Комерческий', 'Комерческий')], default='Население', max_length=30, verbose_name='Абонент'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='type',
            field=models.CharField(choices=[('Активная +', 'Активная +'), ('Активная + / Активная -', 'Активная + / Активная -'), ('Активная + / Реактивная +', 'Активная + / Реактивная +'), ('Активная +- / Реактивная +-', 'Активная +- / Реактивная +-')], default='Активная +', max_length=30, verbose_name='Тип'),
        ),
        migrations.DeleteModel(
            name='CityOrVillage',
        ),
        migrations.DeleteModel(
            name='Faza',
        ),
        migrations.DeleteModel(
            name='Rate',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
