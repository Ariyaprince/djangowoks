from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from menu.models import menu_items

class ItemView(APIView):
    def get(self, request, *args, **kwargs):
        all_items = menu_items
        if "category" in request.query_params:
            category = request.query_params.get("category")
            all_items = [item for item in menu_items if item["category"] == category]
        if "limit" in request.query_params:
            lim = int(request.query_params.get("limit"))
            all_items = all_items[:lim]
            return Response(data=all_items)


        if "rating" in request.query_params:
            rating=int(request.query_params.get("rating"))
            data=[item for item in menu_items if item["rating"]<=rating]
            return Response(data=data)


        return Response(data=menu_items)

    def post(self,request,*args,**kwargs):
        data=request.data
        menu_items.append(data)
        return Response(data=data)

class ItemDetailView(APIView):
    def get(self,request,*args,**kwargs):
        icode=kwargs.get("icode")
        dish=[item for item in menu_items if item["code"]==icode].pop()
        return Response(data=dish)

    def put(self,request,*args,**kwargs):
        icode=kwargs.get("icode")
        dish=[item for item in menu_items if item["code"]==icode].pop()
        dish.update(request.data)
        return Response(data=dish)

    def delete(self,request,*args,**kwargs):
        icode = kwargs.get("icode")
        dish = [item for item in menu_items if item["code"] == icode].pop()
        menu_items.remove(dish)
        return Response(data=dish)




