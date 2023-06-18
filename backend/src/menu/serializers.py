from rest_framework import serializers
from .models import Product, Client, Application


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Application
		fields = ['is_active','id', 'client_name', 'client_tel', 'client_id', 'product_name', 'price', 'total_price', 'total_count', 'date']
