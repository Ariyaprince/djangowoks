from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import items

class ProductView(APIView):
    def get(self,request,*args,**kwargs):

        if "price_lte" in request.query_params:
            price=int(request.query_params.get("price_lte"))
            items_lte=[item for item in items if item["price"]<=price]
            return Response(data=items_lte)

        if "limit" in request.query_params:
            limit=int(request.query_params.get("limit"))
            products=[item for item in items if item["id"]<=limit]
            return Response(data=products)
        return Response(data=items)

    def post(self,request,*args,**kwargs):
        data=request.data
        return Response(data=data)


