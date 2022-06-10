from django.db import models
from user.models import UserModel

# Create your models here.


class CategoryModel(models.Model):
    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.cetegory_name

    cetegory_name = models.CharField(max_length=256)

class ProductModel(models.Model):
    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=256)
    category = models.ManyToManyField(CategoryModel)
    img = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    price = models.IntegerField()
    stock = models.IntegerField()


class OrderStatusModel(models.Model):
    class Meta:
        db_table = "order_status"

    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=256)


class ProductOrderModel(models.Model):
    class Meta:
        db_table = "product_order"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)


class UserOrderModel(models.Model):
    class Meta:
        db_table = "user_order"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    price = models.IntegerField()
    address = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)