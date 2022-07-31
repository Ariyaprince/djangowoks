from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from dishapi.models import Dishes
from dishapi.serializers import DishSerializer
from rest_framework import status

class DishView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializers=DishSerializer(qs,many=True)
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializers=DishSerializer(data=request.data)
        if serializers.is_valid():
            Dishes.objects.create(**serializers.validated_data)
            return Response(data=serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class DishDetailsView(APIView):
    def get(self,*args,**kwargs):
        id=kwargs.get("id")
        qs=Dishes.objects.get(id=id)
        serializers=DishSerializer(qs)
        return Response(data=serializers.data,status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance=Dishes.objects.get(id=id)
        serializers=DishSerializer(data=request.data)
        if serializers.is_valid():
            instance.name=serializers.validated_data.get("name")
            instance.price=serializers.validated_data.get("price")
            instance.category=serializers.validated_data.get("category")
            instance.rating=serializers.validated_data.get("rating")
            instance.save()
            return Response(data=serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        instance = Dishes.objects.get(id=id)
        serializers = DishSerializer(instance)
        instance.delete()
        return Response({"msg":"deleted"},status=status.HTTP_400_BAD_REQUEST)




