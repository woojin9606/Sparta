from rest_framework import serializers
from product.models import Product, Review
from datetime import datetime

class ReviewSerializer(serializers.ModelSerializer):
   class Meta:
        # serializer에 사용될 model, field지정
        model = Review
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
   review_set = serializers.SerializerMethodField()
   rating = serializers.SerializerMethodField('scoresAverage')

   def get_review_set(self, obj):
         review_set = Review.objects.filter(product=obj).order_by("-create_date").first()
         
         if review_set is not None:
            review_set_serializer = ReviewSerializer(review_set)
            return review_set_serializer.data

         return {}


   def scoresAverage(self, obj):
        length = obj.review_set.count()
        if length != 0:
            total = 0
            for review in obj.review_set.all():
                total += review.rating
            result = round(total/length, 2)
        else:
            result = 0
        return result
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
        
        validated_data["description"] += f'{today}에 등록된 상품입니다.'
        product = Product(**validated_data)

        product.save()

        return product

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

   
   