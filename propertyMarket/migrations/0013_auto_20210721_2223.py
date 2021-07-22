# Generated by Django 3.2.5 on 2021-07-21 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertyMarket', '0012_auto_20210721_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(default='frf', upload_to='propertyMarket/images/properties/residential/profiles', verbose_name='profile image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('clinic', 'clinic'), ('chalet', 'chalet'), ('serviced apartment', 'serviced apartment'), ('town house', 'town house'), ('villa', 'villa'), ('apartment', 'apartment'), ('duplex', 'duplex'), ('restaurant', 'restaurant'), ('pent house', 'pent house'), ('Industrial', 'Industrial'), ('office', 'office'), ('retail', 'retail'), ('studio', 'studio'), ('twin house', 'twin house')], max_length=100, verbose_name='Property Type'),
        ),
    ]
