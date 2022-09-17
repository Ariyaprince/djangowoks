from django.urls import path
from todoapp import views

urlpatterns=[
    path("signup",views.SignUpView.as_view()),
    path("login",views.LoginView.as_view()),
]