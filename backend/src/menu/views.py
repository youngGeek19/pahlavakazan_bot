from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Product, Client, Application
from .serializers import ProductSerializer, ClientSerializer, ApplicationSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated



class ProductViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = (IsAdminOrReadOnly, )


class ClientViewSet(viewsets.ModelViewSet):
	queryset = Client.objects.all()
	serializer_class = ClientSerializer
	permission_classes = (IsAdminOrReadOnly, )


class ApplicationViewSet(viewsets.ModelViewSet):
	queryset = Application.objects.all()
	serializer_class = ApplicationSerializer
	permission_classes = (IsAdminOrReadOnly, )


