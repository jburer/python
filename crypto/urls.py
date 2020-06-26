from django.urls import path
from crypto import views

urlpatterns = [
    path("", views.home, name="home"),
    path("python/<data>", views.python, name="python"),
]
