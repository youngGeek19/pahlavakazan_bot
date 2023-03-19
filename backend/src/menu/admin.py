from django.contrib import admin

from . import models



class productsAdmin(admin.ModelAdmin):
	list_display = ['pk', 'name', 'desc', 'price', 'photo']
	list_display_links = ('name',)
	list_editable = ['price']
	search_fields = ('name',)

class clientsAdmin(admin.ModelAdmin):
	list_display = ['pk', 'name', 'tel', 'email']
	list_display_links = ('name',)
	search_fields = ('name',)

class ordersAdmin(admin.ModelAdmin):
	list_display = ['pk', 'get_client_name', 'get_client_tel', 'product', 'date', 'is_active']
	list_display_links = ('get_client_name', 'product')
	search_fields = ('client', 'product')
	date_hierarchy = 'date'
	ordering = ['-date']
	def get_client_name(self, obj):
		return obj.client.name
	def get_client_tel(self, obj):
		return obj.client.tel
	get_client_name.short_description = 'Клиент'
	get_client_tel.short_description = 'Телефон'

admin.site.register(models.Product, productsAdmin)
admin.site.register(models.Client, clientsAdmin)
admin.site.register(models.Order, ordersAdmin)

