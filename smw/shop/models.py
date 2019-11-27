from django.db import models
from django.contrib.auth.models import User
#from django.db import 'django-invoice


class ware_house(models.Model):
	ware_place=models.CharField(max_length=30,unique=True)
	ware_password=models.CharField(max_length=30,default=None)
	
	def __str__(self):
		return (self.ware_place)


class truck(models.Model):
	truck_name=models.CharField(max_length=30,null=False,default=None)
	truck_number=models.CharField(max_length=6,unique=True)
	truck_password=models.CharField(max_length=30,default=None)
	truck_driver=models.CharField(max_length=30)
	truck_village1=models.CharField(max_length=20,null=True)
	truck_village2=models.CharField(max_length=20,null=True)
	truck_village3=models.CharField(max_length=20,null=True)
	t_ware_id=models.ForeignKey(ware_house,related_name='tware_id',on_delete=models.CASCADE,)
	def __str__(self):
		return (self.truck_number)


class item(models.Model):
	item_barcode=models.IntegerField(unique=True,default=None)
	item_name=models.CharField(max_length=30)
	item_price=models.IntegerField()
	item_mnfctr_date=models.DateField(null=True)
	item_expiry_date=models.DateField(null=True)
	item_quantity_ware=models.IntegerField(default=0)
	item_quantity_truck=models.IntegerField(default=0)

	item_comp_name=models.CharField(max_length=30)
	i_ware_id=models.ForeignKey(ware_house,related_name='iware_id',on_delete=models.CASCADE,)
	i_truck_id=models.ForeignKey(truck,related_name='itruck_id',on_delete=models.CASCADE,)
	def __str__(self):
		return (self.item_name)

		
procure_list=[('Banana','Banana'),('Onion','Onion'),('Rice','Rice'),('Ragi','Ragi'),('Corn','Corn'),('Tomato','Tomato'),('Coconut','Coconut'),('Ginger','Ginger'),('Arecanut','Arecanut'),('Grapes','Grapes')]
		
class procure_item(models.Model):
	proc_item=models.CharField(max_length=20,choices=procure_list)
	proc_item_price=models.FloatField()
	proc_quantity = models.IntegerField(default=0)
	proc_total_price = models.FloatField(default=0)
	def __str__(self):
		return (self.proc_item)
	
	
class customer(models.Model):
	cust_name=models.CharField(max_length=30)
	cust_number=models.CharField(max_length=15, unique=True)

	def __str__(self):
		return (self.cust_name)