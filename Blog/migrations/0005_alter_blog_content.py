# Generated by Django 3.2.5 on 2021-09-17 23:22

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Blog content'),
        ),
    ]
