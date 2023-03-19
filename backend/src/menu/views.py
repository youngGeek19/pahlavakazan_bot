from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Product, Order, Client
from .serializers import ProductSerializer, OrderSerializer, ClientSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = (IsAuthenticated, )
	authentication_classes = (TokenAuthentication, )

class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	permission_classes = (IsAuthenticated, )
	authentication_classes = (TokenAuthentication, )



class ClientViewSet(viewsets.ModelViewSet):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer
	permission_classes = (IsAuthenticated, )
	authentication_classes = (TokenAuthentication, )