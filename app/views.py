import sys
import re
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView

from rest_framework.decorators import api_view
from rest_framework.response import Response

import boto3
import boto3.session

from app.forms import LogMessageForm
from app.models import LogMessage
from app.serializers import LogMessageSerializer
from app.forms import AuthenticatorGenerationForm
from app.models import AuthenticatorStorage

from python_library.data.information.algorithm.random_number import random_number
from python_library.data.information.algorithm.random_number.pseudorandom_number import secure_pseudorandom_number

#from python_library.product_service.operations.log.event.event import Event

#from python_library.data.data_transformation.data_confidentiality.hash import derived_secure_hash
#from python_library.data.data_transformation.data_confidentiality.encryption import encryption
from python_library.data.data_transformation.data_confidentiality.hash import secure_hash
from python_library.data.data_transformation.data_confidentiality.hash import hash_alt

#from python_library.identity_and_access.identity.identity import Identity
#from python_library.identity_and_access.identity.authenticator import authenticator_exchange
#from python_library.identity_and_access.identity.authenticator.key.key import Key
#from python_library.identity_and_access.identity.authenticator.key import key_retrieval
#from python_library.identity_and_access.identity.authenticator.key import key_storage
#from python_library.identity_and_access.identity.authenticator.key.shared_key import shared_key_generation
#from python_library.identity_and_access.identity.authenticator.key.asymmetric_key import asymmetric_key_generation
#from python_library.identity_and_access.identity.authenticator.key.private_key import private_key_generation_rsa
#from python_library.identity_and_access.identity.authenticator.key.public_key import public_key_generation_rsa
#from python_library.identity_and_access.identity.authenticator.password import password_generation
#from python_library.identity_and_access.identity.authenticator.authentication_code import authentication_code_generation
#from python_library.identity_and_access.identity.authenticator.authentication_code.asymmetric_authentication_code import asymmetric_authentication_code_creation_rsa
#from python_library.identity_and_access.entitlement import assume_entitlement


# Create your views here.
class HomeListView(ListView):
    """Renders the home page with a list of messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def app(request, data):
    identity = 'User'

    myobject = []
    # myobject.append(derived_secure_hash.derived_secure_hash_def(data))

    my_secure_pseudorandom_number = secure_pseudorandom_number.secure_pseudorandom_number_def(
        31)
    myobject.append(my_secure_pseudorandom_number)

    my_secure_pseudorandom_number = random_number.RandomNumber()
    rannum = my_secure_pseudorandom_number.secure_pseudorandom_number_def(32)
    myobject.append(rannum)

    my_hash = hash_alt.hash_alt_def(data)
    myobject.append(my_hash)

    my_secure_hash = secure_hash.secure_hash_def("md5", data)
    myobject.append(my_secure_hash)

    #myobject.append(encryption.encryption_def(key, data))

    ##Identity and Access##

    # Authenticate Identity
    #session = authenticate_identity.authenticate_identity_def(identity)
    #session = Identity.authenticate_identity(identity)

    # Create Client Connection to Service
    # if session is not None:
    #    client = session.client('kms')

    # Create Key
    #    my_key = Key.create_key(client, identity)
    #    myobject.append(my_key)

    # myobject.append(authenticator_exchange.authenticator_exchange_def(data))
    # myobject.append(asymmetric_key_generation.asymmetric_key_generation_def())
    # myobject.append(private_key_generation_rsa.private_key_generation_rsa_def())

    #rsa_public_key = public_key_generation_rsa.public_key_generation_rsa_def()
    # myobject.append(rsa_public_key)
    # myobject.append(password_generation.password_generation_def())

    #my_authentication_code = authentication_code_generation.authentication_code_generation_def(data, my_key)
    # myobject.append(my_authentication_code)
    # myobject.append(asymmetric_authentication_code_creation_rsa.asymmetric_authentication_code_creation_rsa_def(rsa_public_key))

    #my_retrieved_key = key_retrieval.key_retrieval_def('mysymmetrickey', my_profile_name)
    # myobject.append(my_retrieved_key)

    # my_assumed_entitlement = assume_entitlement.assume_entitlement_def('arn:aws:iam::562241862267:role/IAMSystemAdministrationRole',
    #    'AssumeRoleSession1',
    #    'arn:aws:iam::562241862267:mfa/User2',
    #    '321735')
    # myobject.append(my_assumed_entitlement)

    content = ''
    for x in myobject:
        content += str(x) + ", "

    return render(
        request,
        'app/app.html',
        {
            'data': data,
            'ciphertext': content
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
        return render(request, "app/log_message.html", {"form": form})


@api_view(['GET'])
def log_message_collection(request):
    if request.method == 'GET':
        log_messages = LogMessage.objects.all()
        serializer = LogMessageSerializer(log_messages, many=True)
        return Response(serializer.data)


def authenticator_generation(request):
    form = AuthenticatorGenerationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            my_derived_secure_hash = derived_secure_hash.derived_secure_hash_def(
                form.cleaned_data['authenticator'])
            authenticator = form.save(commit=False)
            authenticator.store_date = datetime.now()
            authenticator.authenticator = my_derived_secure_hash
            authenticator.save()
            return redirect("home")
    else:
        return render(request, "app/authenticator_generation.html", {"form": form})


def about(request):
    return render(request, "app/about.html")


def contact(request):
    return render(request, "app/contact.html")
