# Generated by Django 3.2.5 on 2021-07-28 16:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GoldMark', '0008_auto_20210727_2142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['question']},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['time_posted']},
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name='Blog content'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of posting'),
        ),
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.BooleanField(choices=[(False, 'For rent'), (True, 'For sale')], verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('apartment', 'apartment'), ('Industrial', 'Industrial'), ('villa', 'villa'), ('twin house', 'twin house'), ('town house', 'town house'), ('studio', 'studio'), ('duplex', 'duplex'), ('retail', 'retail'), ('restaurant', 'restaurant'), ('clinic', 'clinic'), ('chalet', 'chalet'), ('serviced apartment', 'serviced apartment'), ('office', 'office'), ('pent house', 'pent house')], max_length=100, verbose_name='Property Type'),
        ),
    ]