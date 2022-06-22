from functools import partial
import imp
from urllib import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from product.models import Product, Review
from django.utils import timezone
from ai.permissions import ProductWriteMoreThanThreeDays
from product.serializers import ProductSerializer
from datetime import datetime
from django.db.models import Q


# Create your views here.
class ProductView(APIView):
    permission_classes = [ProductWriteMoreThanThreeDays]

    def get(self, request):
        today = datetime.now()
        products = Product.objects.filter(
            Q(post_start_date__lte=today, post_end_date__gte=today, is_active=True) |
            Q(user=request.user)
            )
        return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['user'] = request.user.id

        product_serializer = ProductSerializer(data=request.data, context={'requeest':request})
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
            
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, obj_id):
        product = Product.objects.get(id=obj_id)
        
        product_serializer = ProductSerializer(product, data=request.data, partial=True)
        
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
            
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




