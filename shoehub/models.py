from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)

    class Meta:
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name}{self.last_name}'

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.DecimalField(default=0,decimal_places=2,max_digits=50)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description=models.CharField(blank=True,null=True,max_length=100)
    image=models.ImageField(upload_to='uploads/product/')

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.product
