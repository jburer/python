import sys
import re
from datetime import datetime
from django.http import HttpResponse

from python_library.data.data_transformation.data_confidentiality.hash.secure_hash.secure_hash import derived_secure_hash

# Create your views here.
def home(request):
    return HttpResponse("Hello")

def python(request, data):
    myobject = derived_secure_hash.derived_secure_hash_def(data)


    content = ''
    for x in myobject:
        content += str(x) + "<p>"

    return HttpResponse(content)