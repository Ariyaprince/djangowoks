from django.shortcuts import render
# Create your views here.
from django.views.generic import View

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"registration.html")

    def post(self,request,*args,**kwargs):
        print(request.POST.get("firstname"))
        print(request.POST.get("lastname"))
        return render(request,"registration.html")

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")

    def post(self,request,*args,**kwargs):
        print(request.POST.get("username"))
        print(request.POST.get("password"))
        return render(request,"login.html")

