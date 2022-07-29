from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from dishapi.models import Dishes
from dishapi.serializers import DishSerializer

class DishView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Dishes.objects.all()
        serializers=DishSerializer(qs,many=True)
        return Response(data=serializers.data)

    def post(self,request,*args,**kwargs):
        serializers=DishSerializer(data=request.data)
        if serializers.is_valid():
            Dishes.objects.create(**serializers.validated_data)
            return Response(data=serializers.data)
        else:
            return Response(data=serializers.errors)

class DishDetailsView(APIView):
    def get(self,*args,**kwargs):
        id=kwargs.get("id")
        qs=Dishes.objects.get(id=id)
        serializers=DishSerializer(qs)
        return Response(data=serializers.data)

