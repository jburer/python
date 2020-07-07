import sys
import re
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView

from app.forms import LogMessageForm
from app.models import LogMessage
from app.forms import AuthenticatorStorageForm
from app.models import AuthenticatorStorage

from python_library.data.data_transformation.data_confidentiality.encryption import encryption
from python_library.data.data_transformation.data_confidentiality.hash.secure_hash.derived_secure_hash import derived_secure_hash

# Create your views here.
class HomeListView(ListView):
    """Renders the home page with a list of messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def app(request, data):
    myobject = []
    myobject.append(derived_secure_hash.derived_secure_hash_def(data))

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

def store_secret(request):
    form = AuthenticatorStorageForm(request.POST or None)
    #userf = UsersModelForm(request.POST)

    if request.method == "POST":
        if form.is_valid():

            secret = form.save(commit=False)
            #new_user = userf.save(commit=False)

            #password = userf.cleaned_data['password']
            #password = form.cleaned_data['derived_secure_hash']

            my_derived_secure_hash = derived_secure_hash.derived_secure_hash_def(form.cleaned_data['derived_secure_hash'])

            #new_user.password = new1
            #secret.password = my_derived_secure_hash

            #different ways to get the data
            print(form['derived_secure_hash'].value())
            print(form.data['derived_secure_hash'])
            print(form.cleaned_data['derived_secure_hash'])
            print(my_derived_secure_hash)

            #check to see new is saved
            
            print("\n")
            print(secret)
            print("\n")
            secret.store_date = datetime.now()
            secret.derived_secure_hash = my_derived_secure_hash

            #new_user.save()
            secret.save()
            return redirect("home")
    else:
        return render(request, "app/secret.html", {"form" : form})

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")