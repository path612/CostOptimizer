from django.db import models

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

	def __str__(self):
		return self.product_type


class OriginCity(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.DecimalField(max_digits=7, decimal_places=4)
	longitude = models.DecimalField(max_digits=7, decimal_places=4)

	def __str__(self):
		return self.name


class Portcity(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.DecimalField(max_digits=7, decimal_places=4)
	longitude = models.DecimalField(max_digits=7, decimal_places=4)
	is_sea_port = models.BooleanField(default=True)
	# handling_fare = models.Decimalfield(decimal_places=2)

	def __str__(self):
		return self.name


class DestinationCity(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.DecimalField(max_digits=7, decimal_places=4)
	longitude = models.DecimalField(max_digits=7, decimal_places=4)

	def __str__(self):
		return self.name
	


