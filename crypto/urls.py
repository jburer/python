from django.urls import path
from crypto import views

urlpatterns = [
    path("", views.home, name="home"),
    path("crypto/<data>", views.encode, name="encode"),
]
