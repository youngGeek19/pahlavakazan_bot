from django.db import models



class Client(models.Model):
	name = models.CharField(verbose_name = 'Имя', max_length = 50)
	tel = models.CharField(verbose_name = 'Телефон', max_length = 15, unique=True)
	email = models.EmailField(verbose_name = 'Эл. почта', blank=True, max_length = 50, unique=True)


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


	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукты'

class Order(models.Model):
	CHOICES = [
		('active', 'Активный'),
		('deactive', 'Неактивый')
	]
	client = models.ForeignKey(Client, verbose_name = 'Клиент', on_delete=models.CASCADE, related_name = 'client')
	product = models.ForeignKey(Product,verbose_name = 'Продукт', on_delete=models.CASCADE, related_name = 'product')
	date = models.DateTimeField(verbose_name = 'Дата заказа', auto_now = True)
	is_active = models.CharField(verbose_name = 'Статус', choices = CHOICES, max_length = 10)

	def __str__(self):
		return self.client.name 
	class Meta:
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'


