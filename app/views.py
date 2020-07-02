import sys
import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

from python_library.data.data_transformation.data_confidentiality.encryption import encryption

# Create your views here.
def home(request):
    return render(request, "app/home.html")

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