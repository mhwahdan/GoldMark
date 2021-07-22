# Generated by Django 3.2.5 on 2021-07-21 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyMarket', '0007_auto_20210721_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('serviced apartment', 'serviced apartment'), ('office', 'office'), ('town house', 'town house'), ('Industrial', 'Industrial'), ('twin house', 'twin house'), ('retail', 'retail'), ('studio', 'studio'), ('chalet', 'chalet'), ('villa', 'villa'), ('apartment', 'apartment'), ('clinic', 'clinic'), ('duplex', 'duplex'), ('pent house', 'pent house'), ('restaurant', 'restaurant')], max_length=100, verbose_name='Property Type'),
        ),
    ]
