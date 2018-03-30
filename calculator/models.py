from django.db import models
from .choices import *
from django.utils.functional import lazy

class ProductCatagory(models.Model):
	product_type = models.CharField(max_length=50)
	is_bulk = models.BooleanField(default=False)
	gst_rate = models.DecimalField(max_digits=4, decimal_places=2)
	custom_rate = models.DecimalField(max_digits=4, decimal_places=2)
	insurance = models.DecimalField(max_digits=4, decimal_places=2)
	transportable_by_sea = models.BooleanField(default=True)
	transportable_by_road = models.BooleanField(default=True)
	transportable_by_air = models.BooleanField(default=True)
	transportable_by_rail = models.BooleanField(default=True)

	# def __str__(self):
	# 	return self.product_type


class OriginCity(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.DecimalField(max_digits=7, decimal_places=4)
	longitude = models.DecimalField(max_digits=7, decimal_places=4)

	# def __str__(self):
	# 	return self.name


class PortCity(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.DecimalField(max_digits=7, decimal_places=4)
	longitude = models.DecimalField(max_digits=7, decimal_places=4)
	is_sea_port = models.BooleanField(default=True)
	# handling_fare = models.DecimalField(decimal_places=2)

	# def __str__(self):
	# 	return self.name


class DestinationCity(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.DecimalField(max_digits=7, decimal_places=4)
	longitude = models.DecimalField(max_digits=7, decimal_places=4)

	# def __str__(self):
	# 	return self.name
	
class OriginToPortRoad(models.Model):
	city = models.ForeignKey(OriginCity)
	port = models.ForeignKey(PortCity)
	fare_20ST = models.DecimalField(max_digits=10,decimal_places=2)
	fare_40ST = models.DecimalField(max_digits=10,decimal_places=2)
	fare_truck_50_CBM = models.DecimalField(max_digits=10,decimal_places=2)
	fare_truck_70_CBM = models.DecimalField(max_digits=10,decimal_places=2)
	fare_truck_90_CBM = models.DecimalField(max_digits=10,decimal_places=2)

	# def __str__(self):
	# 	return self.city__name + " to " self.port__name + " by Rail"
	
	class Meta:
		unique_together = ('city','port')


class OriginToPortRail(models.Model):
	city = models.ForeignKey(OriginCity)
	port = models.ForeignKey(PortCity)
	fare_20ST = models.DecimalField(max_digits=10,decimal_places=2)
	fare_40ST = models.DecimalField(max_digits=10,decimal_places=2)
	fare_freight = models.DecimalField(max_digits=10,decimal_places=2)
	fare_tank = models.DecimalField(max_digits=10,decimal_places=2)
	fare_covered = models.DecimalField(max_digits=10,decimal_places=2)
	fare_hopper = models.DecimalField(max_digits=10,decimal_places=2)
	# fare_box_density = models.DecimalField(max_digits=10, decimal_places=2)


	class Meta:
		unique_together = ('city','port')


class OriginToPortAir(models.Model):
	city = models.ForeignKey(OriginCity)
	port = models.ForeignKey(PortCity)
	fare_box_density = models.DecimalField(max_digits=10, decimal_places=2)


	class Meta:
		unique_together = ('city','port')

# class OriginToPort(object):
# 	city = models.ForeignKey(OriginCity)
# 	port = models.ForeignKey(PortCity)
# 	transportation_choice = models.IntegerField(choices=OriginToPortTransportationModeChoices)
# 	container_type = models.IntegerField(default=1)


class PortToDestinationAir(models.Model):
	city = models.ForeignKey(DestinationCity)
	port = models.ForeignKey(PortCity)
	fare_box_density = models.DecimalField(max_digits=10, decimal_places=2)
	

	class Meta:
		unique_together = ('city','port')


class PortToDestinationRoad(models.Model):
	city = models.ForeignKey(DestinationCity)
	port = models.ForeignKey(PortCity)
	fare_20ST = models.DecimalField(max_digits=10,decimal_places=2)
	fare_40ST = models.DecimalField(max_digits=10,decimal_places=2)
	fare_truck_50_CBM = models.DecimalField(max_digits=10,decimal_places=2)
	fare_truck_70_CBM = models.DecimalField(max_digits=10,decimal_places=2)
	fare_truck_90_CBM = models.DecimalField(max_digits=10,decimal_places=2)

	
	class Meta:
		unique_together = ('city','port')


class PortToDestinationSea(models.Model):
	city = models.ForeignKey(DestinationCity)
	port = models.ForeignKey(PortCity)
	fare_20ST = models.DecimalField(max_digits=10,decimal_places=2)
	fare_40ST = models.DecimalField(max_digits=10,decimal_places=2)
	fare_bulk_20k_DWT = models.DecimalField(max_digits=10, decimal_places=2)
	fare_bulk_40k_DWT = models.DecimalField(max_digits=10, decimal_places=2)
	fare_bulk_70k_DWT = models.DecimalField(max_digits=10, decimal_places=2)


	class Meta:
		unique_together = ('city','port')

def help_domestic_container_choices():
	RailModeChoices = (
		(1, "20'ST"),
		(2, "40'ST"),
		(3, "Freight"),
		(4, "Tank"),
		(5, "Covered"),
		(6, "Hopper"),
		)


	RoadModeChoices = (
		(1, "20'ST"),
		(2, "40'ST"),
		(3, "Truck 50CBM"),
		(4, "Truck 70CBM"),
		(5, "Truck 90CBM"),
		)


	AirModeChoices = (
		(1, "Crates"),
		)
	return choice(RailModeChoices + RoadModeChoices + AirModeChoices)
	
def help_foreign_container_choices():
	WaterModeChoices = (
		(1, "20'ST"),
		(2, "40'ST"),
		(3, "Freight"),
		(4, "Tank"),
		(5, "Covered"),
		(6, "Hopper"),
		)


	RoadModeChoices = (
		(1, "20'ST"),
		(2, "40'ST"),
		(3, "Truck 50CBM"),
		(4, "Truck 70CBM"),
		(5, "Truck 90CBM"),
		)


	AirModeChoices = (
		(1, "Crates"),
		)
	return choice(RailModeChoices + RoadModeChoices + AirModeChoices)
	
class CalculatorData(models.Model):
	origin_city = models.ForeignKey(OriginCity)
	port_city = models.ForeignKey(PortCity)
	destination_city = models.ForeignKey(DestinationCity)
	product_catagory = models.ForeignKey(ProductCatagory)
	manufacturing_fare = models.DecimalField(max_digits=10,decimal_places=2)
	origin_to_port_method = models.IntegerField(choices=OriginToPortTransportationModeChoices)
	origin_to_port_container_type = models.IntegerField(default=1)
	port_to_dest_container_type = models.IntegerField(default=1)
	port_to_dest_method = models.IntegerField(choices=PortToDestinationTransportationModeChoices)
	origin_to_port_fare = models.DecimalField(max_digits=10,decimal_places=2)
	port_to_dest_fare = models.DecimalField(max_digits=10,decimal_places=2)
	gst_fare = models.DecimalField(max_digits=10,decimal_places=2)
	customs_fare = models.DecimalField(max_digits=10,decimal_places=2)
	insurance_fare = models.DecimalField(max_digits=10,decimal_places=2)
	total_fare = models.DecimalField(max_digits=10,decimal_places=2)