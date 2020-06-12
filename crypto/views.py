import sys
import re
from datetime import datetime
from django.http import HttpResponse
from python.encoding import encoding

# Create your views here.
def home(request):
    return HttpResponse("Hello")

def encode(request, data):
    encoded_object = encoding.encode_object(data)


    content = ''
    for x in encoded_object:
        content += str(x) + " and is of type " + str(type(x).__name__) + "<p>"

    return HttpResponse(content)