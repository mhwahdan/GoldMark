# Generated by Django 3.2.5 on 2021-07-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoldMark', '0003_auto_20210725_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('studio', 'studio'), ('town house', 'town house'), ('pent house', 'pent house'), ('chalet', 'chalet'), ('duplex', 'duplex'), ('apartment', 'apartment'), ('villa', 'villa'), ('Industrial', 'Industrial'), ('office', 'office'), ('twin house', 'twin house'), ('restaurant', 'restaurant'), ('retail', 'retail'), ('serviced apartment', 'serviced apartment'), ('clinic', 'clinic')], max_length=100, verbose_name='Property Type'),
        ),
    ]
