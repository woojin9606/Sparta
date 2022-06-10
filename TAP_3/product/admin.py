from django.contrib import admin
from .models import CategoryModel, ProductModel, OrderStatusModel, ProductOrderModel, UserOrderModel
# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(OrderStatusModel)
admin.site.register(ProductOrderModel)
admin.site.register(UserOrderModel)
