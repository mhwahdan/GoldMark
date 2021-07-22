# Generated by Django 3.2.5 on 2021-07-22 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyMarket', '0014_auto_20210722_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='interest',
            field=models.FloatField(default=3.5, verbose_name='Bank interest rate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('serviced apartment', 'serviced apartment'), ('restaurant', 'restaurant'), ('retail', 'retail'), ('apartment', 'apartment'), ('chalet', 'chalet'), ('duplex', 'duplex'), ('pent house', 'pent house'), ('Industrial', 'Industrial'), ('twin house', 'twin house'), ('clinic', 'clinic'), ('town house', 'town house'), ('office', 'office'), ('villa', 'villa'), ('studio', 'studio')], max_length=100, verbose_name='Property Type'),
        ),
    ]
