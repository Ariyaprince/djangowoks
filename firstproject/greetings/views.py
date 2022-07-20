from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.views import Response
from datetime import datetime
class GoodMorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"good morning"})

class GoodAfternoonView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"good afternoon "})

class GreetingsView(APIView):
    def get(self,request,*args,**kwargs):
        c_date=datetime.now()
        c_hour=c_date.hour
        greetings=""
        if c_hour<12:
            greetings="good morning"
        elif c_hour<18:
            greetings="good afternoon"
        elif c_hour<24:
            greetings="good evening"
        return Response({"msg":greetings})
