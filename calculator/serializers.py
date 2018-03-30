from .models import CalculatorData
from rest_framework import serializers

class CalculatorSerializer(serializers.ModelSerializer):
	class Meta:
		model = CalculatorData
		fields = (
			'origin_city',
			'port_city',
			'destination_city',
			'product_catagory',
			'origin_to_port_method',
			'origin_to_port_container_type',
			'port_to_dest_method',
			'port_to_dest_container_type',
			'manufacturing_fare'
			)


class CalculatorFullSerializer(serializers.ModelSerializer):
	class Meta:
		model = CalculatorData
		fields = '__all__'