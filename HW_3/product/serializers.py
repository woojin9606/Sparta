import imp
from rest_framework import serializers
from product.models import Product
from datetime import datetime


class ProductSerializer(serializers.ModelSerializer):

   # validate 함수 선언 시 serializer에서 자동으로 해당 함수의 validation을 해줌
   def validate(self, data):
      today = datetime.today().strftime("%Y-%m-%d")
      if str(data.get("post_end_date")) < today:
         # validation에 통과하지 못할 경우 ValidationError class 호출
         raise serializers.ValidationError(
           # custom validation error message
           detail={"error": "노출 일자가 지났습니다."},
         )

      # validation에 문제가 없을 경우 data return
      return data

   def create(self, validated_data):     
        # User object 생성
        today = datetime.today().strftime("%Y-%m-%d")
        validated_data["description"] += f' {today}에 등록된 상품입니다.'
        product = Product(**validated_data)
        product.save()
        return validated_data

   def update(self, instance, validated_data):
      today = datetime.today().strftime("%Y-%m-%d")
      for key, value in validated_data.items():
         if key == "description":
            value += f' {today}에 수정된 상품입니다.'
            continue            
         setattr(instance, key, value)
      instance.save()
      return instance



   class Meta:
        model = Product
        fields = "__all__"

