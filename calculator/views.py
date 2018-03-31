from django.shortcuts import render
from .models import *
from .serializers import CalculatorSerializer, CalculatorFullSerializer
from rest_framework.views import APIView
from .functions import origin_port_fare, port_destination_fare
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
# Create your views here.

class Calculator(APIView):
	def get(self, request, format=None):
		calc_datas = CalculatorData.objects.all()
		serializer = CalculatorFullSerializer(calc_datas, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CalculatorSerializer(data = request.data)
		print(serializer)
		if serializer.is_valid():
			print(serializer)
			calcobj = CalculatorData()
			szr = serializer.data
			# print("Fare: " + origin_port_fare(serializer))
			calcobj.origin_city = OriginCity.objects.get(id = szr['origin_city'])
			calcobj.port_city = PortCity.objects.get(id = szr['port_city'])
			calcobj.destination_city = DestinationCity.objects.get(id = szr['destination_city'])
			calcobj.product_catagory = ProductCatagory.objects.get(id = szr['product_catagory'])
			calcobj.origin_to_port_method = szr['origin_to_port_method']
			calcobj.origin_to_port_container_type = szr['origin_to_port_container_type']
			calcobj.port_to_dest_method = szr['port_to_dest_method']
			calcobj.port_to_dest_container_type = szr['port_to_dest_container_type']
			calcobj.manufacturing_fare = szr['manufacturing_fare']
			calcobj.origin_to_port_fare = origin_port_fare(szr)
			calcobj.port_to_dest_fare = port_destination_fare(szr)
			calcobj.gst_fare = float(calcobj.manufacturing_fare) * float(calcobj.product_catagory.gst_rate) / 100
			calcobj.customs_fare = float(calcobj.manufacturing_fare) * float(calcobj.product_catagory.custom_rate) / 100
			calcobj.insurance_fare = float(calcobj.manufacturing_fare) * float(calcobj.product_catagory.insurance) / 100
			calcobj.total_fare = float(calcobj.manufacturing_fare) + float(calcobj.origin_to_port_fare) + float(calcobj.port_to_dest_fare) + \
									float(calcobj.gst_fare) + float(calcobj.customs_fare) + float(calcobj.insurance_fare)
			calcobj.save()
			slzr = CalculatorFullSerializer(calcobj)
			return Response(slzr.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)