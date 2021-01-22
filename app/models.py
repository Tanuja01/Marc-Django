from django.db import models

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=100)
	price = models.FloatField()	
	quantity = models.IntegerField()


class Order(models.Model):
	product = models.ForeignKey(Product,null=True,on_delete = models.SET_NULL,related_name ='product_related') #models.CASCADE , models.SET_NULL
	order_date = models.DateTimeField(auto_now = True)
	quantity_purchased = models.IntegerField()


