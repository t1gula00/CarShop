# Generated by Django 2.1.7 on 2019-04-04 07:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('car_brand', models.CharField(max_length=200)),
                ('car_type', models.CharField(max_length=200)),
                ('engine_size', models.IntegerField()),
                ('km_driven', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=200)),
                ('gear_type', models.CharField(max_length=200)),
                ('year_model', models.IntegerField()),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtors', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
    ]