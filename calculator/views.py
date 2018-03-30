from django.shortcuts import render
from .models import CalculatorData
from .serializers import CalculatorSerializer
from rest_framework.views import APIView
# Create your views here.

class Calculator(APIView):
	
	def post(self, request, format=None):
		serializer = CalculatorSerializer(data = request.data)
		if serializer.is_valid:
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)			
