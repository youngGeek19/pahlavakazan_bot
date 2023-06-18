from django.db import models



class Client(models.Model):
	name = models.CharField(verbose_name = 'Имя', max_length = 50)
	tel = models.CharField(verbose_name = 'Телефон', max_length = 15, unique=True)
	user_id = models.CharField(verbose_name ='ЮзерID', max_length = 100, null=True)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Клиент'
		verbose_name_plural = 'Клиенты'


class Product(models.Model):
	name = models.CharField(verbose_name = 'Название', max_length = 50)
	desc = models.TextField(verbose_name = 'Описание', max_length = 250)
	price = models.PositiveSmallIntegerField(verbose_name = 'Цена за кг')
	photo = models.ImageField(upload_to = 'media/',verbose_name = 'Изображение')
	available = models.PositiveSmallIntegerField(verbose_name = 'Количество в наличии', null=True)


	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'



class Application(models.Model):
	CHOICES = [
		('active', 'Активный'),
		('deactive', 'Неактивый')
	]
	client_name = models.CharField(verbose_name = 'Клиент', max_length=20)
	client_tel = models.CharField(verbose_name = 'Телефон', max_length = 15) 
	client_id = models.PositiveSmallIntegerField(verbose_name='Telegram-ID')
	product_name = models.CharField(verbose_name = 'Продукт',  max_length=50)
	date = models.DateTimeField(verbose_name = 'Дата заказа', auto_now = True)
	price = models.PositiveSmallIntegerField(verbose_name = 'Цена за упаковку')
	total_count = models.PositiveSmallIntegerField(verbose_name = 'Количество')
	total_price = models.PositiveSmallIntegerField(verbose_name = 'Итоговая цена')
	is_active = models.CharField(verbose_name = 'Статус', choices = CHOICES, max_length = 10, default='active')

	def __str__(self):
		return self.client_name + ' ' + self.product_name 
	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

