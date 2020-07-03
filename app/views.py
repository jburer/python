import sys
import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from app.forms import LogMessageForm
from app.models import LogMessage
from django.views.generic import ListView

from python_library.data.data_transformation.data_confidentiality.encryption import encryption

# Create your views here.
def home(request):
    return render(request, "app/home.html")

class HomeListView(ListView):
    """Renders the home page with a list of messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

def app(request, data):
    myobject = []
    myobject.append(encryption.encryption_def(data))

    content = ''
    for x in myobject:
        content += str(x)

    return render(
        request,
        'app/app.html',
        {
            'data' : data,
            'ciphertext' : content
        }
    )

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "app/log_message.html", {"form" : form})
        