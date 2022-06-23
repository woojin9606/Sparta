from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from item.serializers import ItemSerializer
from item.models import Item


# Create your views here.

class ItemView(APIView):

    def get(self, request):
        print(request.data)
        item = Item.objects.all()
        serialized_item_data = ItemSerializer(item, many=True)
        return Response(serialized_item_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        item_serializer = ItemSerializer(data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response(item_serializer.data, status=status.HTTP_200_OK)

        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
