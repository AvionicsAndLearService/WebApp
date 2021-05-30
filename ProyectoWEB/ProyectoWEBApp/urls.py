from django.urls import path
from ProyectoWEBApp import views

urlpatterns = [
    path("", views.Home, name="Home"),
    path("admin", views.Admin, name="Admin"),
    path("ot", views.OT, name="OT"),
    path("almacen", views.Almacen, name="Almacen"),
    path("blog", views.Blog, name="Blog"),
]
