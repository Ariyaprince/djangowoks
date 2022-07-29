from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from productapi.models import Product
from productapi.serializers import ProductSerializer

class ProductView(APIView):
    def get(self,*args,**kwargs):
        qs=Product.objects.all()
        serializer=ProductSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializers=ProductSerializer(data=request.data)
        if serializers.is_valid():
            Product.objects.create(**serializers.validated_data)
            return Response(data=serializers.data)
        else:
            return Response(data=serializers.errors)

class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Product.objects.get(id=id)
        serializer=ProductSerializer(qs)
        return Response(data=serializer.data)


