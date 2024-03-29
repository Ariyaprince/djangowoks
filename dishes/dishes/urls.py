"""dishes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dishapi.views import DishView,DishDetailsView,DishModelView,DishDetailModelView,DishSetModelView,DishesModelViwsetViews,UserModelViewsetView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router=DefaultRouter()
router.register('api/v3/dishes',DishSetModelView,basename="dishes")
router.register('api/v4/dishes',DishesModelViwsetViews,basename="mdishes")
router.register('api/v5/signin',UserModelViewsetView,basename="user")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dishes/',DishView.as_view()),
    path('dishes/<int:id>',DishDetailsView.as_view()),
    path('api/v2/dishes/',DishModelView.as_view()),
    path('api/v2/dishes/<int:id>',DishDetailModelView.as_view()),
    path('api/v4/token',obtain_auth_token)
]+router.urls
