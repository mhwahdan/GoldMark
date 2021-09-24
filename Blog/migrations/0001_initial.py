# Generated by Django 3.2.5 on 2021-09-15 23:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Blog name')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of posting')),
                ('image', models.ImageField(upload_to='propetyMarket/images/Blog/main/', verbose_name='Blog image')),
                ('content', models.TextField(verbose_name='Blog content')),
                ('description', models.TextField(verbose_name='Blog description')),
            ],
            options={
                'ordering': ['date_posted'],
            },
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Category name')),
            ],
        ),
    ]
