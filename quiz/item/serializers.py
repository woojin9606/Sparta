from rest_framework import serializers
from item.models import Category, Item, ItemOrder, Order

class CategorySerializer(serializers.ModelSerializer):
   class Meta:
        model = Category
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Item
        fields = "__all__"

class ItemOrderSerializer(serializers.ModelSerializer):
   class Meta:
        model = ItemOrder
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
   class Meta:
        model = Order
        fields = "__all__"