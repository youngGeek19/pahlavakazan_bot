from django.contrib import admin

from . import models



class productsAdmin(admin.ModelAdmin):
	list_display = ['pk', 'name', 'desc', 'price', 'photo']
	list_display_links = ('name',)
	list_editable = ['price']
	search_fields = ('name',)

class clientsAdmin(admin.ModelAdmin):
	list_display = ['pk', 'name', 'tel', 'user_id']
	list_display_links = ('name',)
	search_fields = ('name',)

class applicationAdmin(admin.ModelAdmin):
	list_display = ['pk', 'client_name', 'client_tel', 'product_name', 'price', 'total_count', 'total_price', 'date', 'is_active']
	list_display_links = ('client_name', 'product_name')
	list_editable = ['is_active']
	search_fields = ('client_name', 'product_name')
	date_hierarchy = 'date'
	ordering = ['-date']

admin.site.register(models.Product, productsAdmin)
admin.site.register(models.Client, clientsAdmin)
admin.site.register(models.Application, applicationAdmin)

