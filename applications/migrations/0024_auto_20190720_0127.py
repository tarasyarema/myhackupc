# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-19 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0023_auto_20190719_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='tshirt_size',
            field=models.CharField(choices=[('XS', 'Unisex - XS'), ('S', 'Unisex - S'), ('M', 'Unisex - M'), ('L', 'Unisex - L'), ('XL', 'Unisex - XL'), ('XXL', 'Unisex - XXL'), ('XXXL', 'Unisex - XXXL')], default='M', max_length=5),
        ),
    ]