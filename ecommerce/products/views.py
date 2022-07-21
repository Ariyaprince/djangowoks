from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import items

class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data=items)
    def post(self,request,*args,**kwargs):
        data=request.data
        return Response(data=data)


