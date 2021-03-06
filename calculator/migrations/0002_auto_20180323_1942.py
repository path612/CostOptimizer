# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalculatorData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_to_port_method', models.IntegerField(choices=[(1, 'Road'), (2, 'Rail'), (3, 'Air')])),
                ('origin_to_port_container_type', models.IntegerField(choices=[(1, "20'ST"), (2, "40'ST"), (3, 'Freight'), (4, 'Tank'), (5, 'Covered'), (6, 'Hopper')])),
                ('port_to_dest_container_type', models.IntegerField(choices=[(1, "20'ST"), (2, "40'ST"), (3, 'Bulk 20k DWT'), (4, 'Bulk 40k DWT'), (5, 'Bulk 70k DWT'), (6, 'Crates')])),
                ('port_to_dest_method', models.IntegerField(choices=[(1, 'Road'), (2, 'Sea'), (3, 'Air')])),
                ('manufacturing_fare', models.DecimalField(decimal_places=2, max_digits=10)),
                ('origin_to_port_fare', models.DecimalField(decimal_places=2, max_digits=10)),
                ('port_to_dest_fare', models.DecimalField(decimal_places=2, max_digits=10)),
                ('destination_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.DestinationCity')),
                ('origin_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.OriginCity')),
                ('port_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Portcity')),
                ('product_catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.ProductCatagory')),
            ],
        ),
        migrations.CreateModel(
            name='OriginToPortAir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_box_density', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.OriginCity')),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Portcity')),
            ],
        ),
        migrations.CreateModel(
            name='OriginToPortRail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_20ST', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_40ST', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_freight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_tank', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_covered', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_hopper', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.OriginCity')),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Portcity')),
            ],
        ),
        migrations.CreateModel(
            name='OriginToPortRoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_20ST', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_40ST', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_box_density', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_truck_50_CBM', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_truck_70_CBM', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_truck_90_CBM', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.OriginCity')),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Portcity')),
            ],
        ),
        migrations.CreateModel(
            name='PortToDestinationAir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_box_density', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.DestinationCity')),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Portcity')),
            ],
        ),
        migrations.CreateModel(
            name='PortToDestinationRoad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_20ST', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_40ST', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_box_density', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_truck_50_CBM', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_truck_70_CBM', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_truck_90_CBM', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.DestinationCity')),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Portcity')),
            ],
        ),
        migrations.CreateModel(
            name='PortToDestinationSea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_20ST', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_40ST', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_box_density', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_bulk_20k_DWT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_bulk_40k_DWT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fare_bulk_70k_DWT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.DestinationCity')),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.Portcity')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='porttodestinationsea',
            unique_together=set([('city', 'port')]),
        ),
        migrations.AlterUniqueTogether(
            name='porttodestinationroad',
            unique_together=set([('city', 'port')]),
        ),
        migrations.AlterUniqueTogether(
            name='porttodestinationair',
            unique_together=set([('city', 'port')]),
        ),
        migrations.AlterUniqueTogether(
            name='origintoportroad',
            unique_together=set([('city', 'port')]),
        ),
        migrations.AlterUniqueTogether(
            name='origintoportrail',
            unique_together=set([('city', 'port')]),
        ),
        migrations.AlterUniqueTogether(
            name='origintoportair',
            unique_together=set([('city', 'port')]),
        ),
    ]
