from django.urls import path
from app import views
from app.models import AuthenticatorStorage

home_list_view = views.HomeListView.as_view(
    queryset=AuthenticatorStorage.objects.order_by("-store_date")[:5], 
    context_object_name = "authenticator_list",
    template_name = "app/home.html"
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("app/<data>", views.app, name="app"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
    path("authenticator_generation/", views.authenticator_generation, name="authenticator_generation"),
]
