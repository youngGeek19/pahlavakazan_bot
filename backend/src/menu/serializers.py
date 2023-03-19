from rest_framework import serializers
from .models import Product, Order, Client


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('name', 'desc', 'price',)

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ('client', 'product', 'date', 'is_active')

class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = ('name', 'tel', 'email')