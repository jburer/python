""" Module for Creation of Authentication Code
Using a Private for RSA, commonly called 'signing' """

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from python_library.identity_and_access.identity.authenticator.key.private_key import private_key_retrieval_rsa
from python_library.product_service.operations.log import log

def asymmetric_authentication_code_creation_rsa_def(data):
    """ Asymmetric Authentication Code Creation Function for RSA """

    try:
        print('\n')
        print(data)
        print('\n')

        pem = data.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        print('\n')
        print(pem)
        print('\n')
        
        # Import private key
        private_key = private_key_retrieval_rsa.private_key_retrieval_rsa_def()

        print('\n')
        print(private_key)
        print('\n')

        asymmetric_authentication_code = private_key.sign(
            pem,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
                ),
            hashes.SHA256()
        )

        print('\n')
        print(asymmetric_authentication_code)
        print('\n')

        return asymmetric_authentication_code
    except Exception as err:
        log.logger.debug(err, exc_info=True)
