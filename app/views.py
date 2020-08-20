import sys
import re
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView

from app.forms import LogMessageForm
from app.models import LogMessage
from app.forms import AuthenticatorGenerationForm
from app.models import AuthenticatorStorage

#from python_library.data.data_transformation.data_confidentiality.encryption import encryption
#from python_library.data.data_transformation.data_confidentiality.hash.secure_hash.derived_secure_hash import derived_secure_hash
#from python_library.identity_and_access.identity.authenticator import authenticator_exchange
#from python_library.identity_and_access.identity.authenticator.key.shared_key import shared_key_generation
#from python_library.identity_and_access.identity.authenticator.key.asymmetric_key import asymmetric_key_generation
#from python_library.identity_and_access.identity.authenticator.password import password_generation
from python_library.data.information.algorithm.random_number.pseudorandom_number import secure_pseudorandom_number
from python_library.data.data_transformation.data_confidentiality.hash import hash_alt
from python_library.data.data_transformation.data_confidentiality.hash import secure_hash
from python_library.data.data_transformation.data_confidentiality.encryption import encryption

# Create your views here.
class HomeListView(ListView):
    """Renders the home page with a list of messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def app(request, data):
    myobject = []
    #myobject.append(derived_secure_hash.derived_secure_hash_def(data))
    #myobject.append(authenticator_exchange.authenticator_exchange_def(data))
    #myobject.append(symmetric_key_generation.symmetric_key_generation_def())
    #myobject.append(asymmetric_key_generation.asymmetric_key_generation_def())
    #myobject.append(password_generation.password_generation_def())
    myobject.append(secure_pseudorandom_number.secure_pseudorandom_number_def(31))
    myobject.append(hash_alt.hash_alt_def(data))
    myobject.append(secure_hash.secure_hash_def("md5", data))
    myobject.append(encryption.encryption_def(key, data))

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

def authenticator_generation(request):
    form = AuthenticatorGenerationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            my_derived_secure_hash = derived_secure_hash.derived_secure_hash_def(form.cleaned_data['authenticator'])
            authenticator = form.save(commit=False)
            authenticator.store_date = datetime.now()
            authenticator.authenticator = my_derived_secure_hash
            authenticator.save()
            return redirect("home")
    else:
        return render(request, "app/authenticator_generation.html", {"form" : form})

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")