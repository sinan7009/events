# Generated by Django 5.1.7 on 2025-03-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True, verbose_name='web address'),
        ),
    ]
