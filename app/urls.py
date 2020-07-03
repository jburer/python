from django.urls import path
from app import views
from app.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5], 
    context_object_name = "message_list",
    template_name = "app/home.html"
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("app/<data>", views.app, name="app"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("log/", views.log_message, name="log"),
]