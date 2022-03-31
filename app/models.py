from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')


class Category(models.Model):
    code = models.CharField(max_length=30, unique=True, verbose_name="Mã")
    name = models.CharField(max_length=200, verbose_name="Tên")

    def __str__(self): return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Nhóm sản phẩm", on_delete=models.PROTECT)
    code = models.CharField(max_length=30, unique=True, verbose_name="Mã")
    name = models.CharField(max_length=200, verbose_name="Tên")
    price = models.IntegerField(verbose_name="Đơn giá")
    image = models.ImageField(blank=True, upload_to="static/images", verbose_name="Ảnh")

    def __str__(self): return self.name


class Order(models.Model):
    class Status:
        PENDING = 0
        DELIVERED = 1
        CANCELLED = 2

    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.IntegerField()
    priceUnit = models.IntegerField()
    total = models.IntegerField()
    customerName = models.CharField(max_length=50)
    customerPhone = models.CharField(max_length=20)
    customerAddress = models.CharField(max_length=200)
    orderDate = models.DateTimeField()
    deliverDate = models.DateTimeField(null=True)
    status = models.IntegerField()
