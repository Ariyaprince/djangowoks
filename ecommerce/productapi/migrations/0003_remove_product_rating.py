# Generated by Django 4.0.6 on 2022-08-08 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapi', '0002_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]
