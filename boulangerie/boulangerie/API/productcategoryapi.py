from ..serializers import (ProductCategorySerializer)
from ..models import  ProductCategory
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProductCategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        productcategories = ProductCategory.objects.filter(available_on_website= True)
        serializer = ProductCategorySerializer(productcategories, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):

        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request,pk ,format=None):
        snippet = ProductCategory.objects.filter(id=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request,pk, format=None):
        
        snippet = ProductCategory.objects.get(name=request.data['name'])
        serializer = ProductCategorySerializer(snippet, data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


