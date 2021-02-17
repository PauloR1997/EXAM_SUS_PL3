"""SUSTILP3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('inicio/',views.index, name="inicio"),

    path('listar_region/', views.listar_region, name="listar_region"),
    path('create-full-region/',views.create_full_region, name="create_full_region"),
    path('eliminar_region/<int:id>',views.eliminar_region, name="eliminar_region"),
    path('save-region/',views.save_region, name="save_region"),
    path('listar_empleado/', views.listar_empleado, name="listar_empleado"),
    path('create-full-empleado/',views.create_full_empleado, name="create_full_empleado"),
]
