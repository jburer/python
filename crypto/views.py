import sys
import re
from datetime import datetime
from django.http import HttpResponse

from python_library.data.data_transformation.data_confidentiality.encryption import encryption

# Create your views here.
def home(request):
    return HttpResponse("Hello")

def python(request, data):
    myobject = []
    myobject.append(encryption.encryption_def(data))


    content = ''
    for x in myobject:
        content += str(x) + "<p>"

    return HttpResponse(content)