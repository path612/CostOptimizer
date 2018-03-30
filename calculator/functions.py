from .models import *
import decimal

def origin_port_fare(dict):
	origin = OriginCity.objects.get(id = dict['origin_city'])
	port = PortCity.objects.get(id = dict['port_city'])
	product = ProductCatagory.objects.get(id = dict['product_catagory'])

	fare = 0
	if dict['origin_to_port_method'] == 1:
		o_to_p_road_fare = OriginToPortRoad.objects.get(city = origin, port = port)
		if dict['origin_to_port_container_type'] == 1:
			fare = o_to_p_road_fare.fare_20ST
		elif dict['origin_to_port_container_type'] == 2:
			fare = o_to_p_road_fare.fare_40ST
		elif dict['origin_to_port_container_type'] == 3:
			fare = o_to_p_road_fare.fare_truck_50_CBM
		elif dict['origin_to_port_container_type'] == 4:
			fare = o_to_p_road_fare.fare_truck_70_CBM
		else:
			fare = o_to_p_road_fare.fare_truck_90_CBM

	elif dict['origin_to_port_method'] == 2:
		o_to_p_rail_fare = OriginToPortRail.objects.get(city = origin, port = port)
		if dict['origin_to_port_container_type'] == 1:
			fare = o_to_p_rail_fare.fare_20ST
		elif dict['origin_to_port_container_type'] == 2:
			fare = o_to_p_rail_fare.fare_40ST
		elif dict['origin_to_port_container_type'] == 3:
			fare = o_to_p_rail_fare.fare_freight
		elif dict['origin_to_port_container_type'] == 4:
			fare = o_to_p_rail_fare.fare_tank
		elif dict['origin_to_port_container_type'] == 4:
			fare = o_to_p_rail_fare.fare_covered
		else:
			fare = o_to_p_rail_fare.fare_hopper

	return float(decimal.Decimal(fare))

def port_destination_fare(dict):
	port = PortCity.objects.get(id = dict['port_city'])
	destination = DestinationCity.objects.get(id = dict['destination_city'])
	product = ProductCatagory.objects.get(id = dict['product_catagory'])
	fare = 0.0
	if dict['port_to_dest_method'] == 1:
		o_to_p_road_fare = PortToDestinationRoad.objects.get(city = destination, port = port)
		if dict['port_to_dest_container_type'] == 1:
			fare = o_to_p_road_fare.fare_20ST
		elif dict['port_to_dest_container_type'] == 2:
			fare = o_to_p_road_fare.fare_40ST
		elif dict['port_to_dest_container_type'] == 3:
			fare = o_to_p_road_fare.fare_truck_50_CBM
		elif dict['port_to_dest_container_type'] == 4:
			fare = o_to_p_road_fare.fare_truck_70_CBM
		else:
			fare = o_to_p_road_fare.fare_truck_90_CBM

	if dict['port_to_dest_method'] == 2:
		o_to_p_road_fare = PortToDestinationSea.objects.get(city = destination, port = port)
		if dict['port_to_dest_container_type'] == 1:
			fare = o_to_p_road_fare.fare_20ST
		elif dict['port_to_dest_container_type'] == 2:
			fare = o_to_p_road_fare.fare_40ST
		elif dict['port_to_dest_container_type'] == 3:
			fare = o_to_p_road_fare.fare_bulk_20k_DWT
		elif dict['port_to_dest_container_type'] == 4:
			fare = o_to_p_road_fare.fare_bulk_40k_DWT
		else:
			fare = o_to_p_road_fare.fare_bulk_70k_DWT

	return float(decimal.Decimal(fare))

