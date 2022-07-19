from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.views import Response

class GoodMorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"good morning"})

class GoodAfternoonView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"good afternoon "})
