# Generated by Django 3.2.5 on 2021-09-17 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propetyMarket', '0004_auto_20210917_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('Industrial', 'Industrial'), ('retail', 'retail'), ('town house', 'town house'), ('clinic', 'clinic'), ('villa', 'villa'), ('serviced apartment', 'serviced apartment'), ('twin house', 'twin house'), ('studio', 'studio'), ('pent house', 'pent house'), ('office', 'office'), ('apartment', 'apartment'), ('duplex', 'duplex'), ('restaurant', 'restaurant'), ('chalet', 'chalet')], max_length=100, verbose_name='Property Type'),
        ),
    ]
