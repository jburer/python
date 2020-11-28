""" Public Key Generation Module using RSA """

#from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
#from cryptography.hazmat.primitives.asymmetric import rsa

from python_library.product_service.operations.log import log
#from python_library.product_service.operations.log.event import event

def public_key_generation_rsa_def():
    """ Public Key Generation Function using RSA """

    try:
        # Import private key
        with open("private.pem", "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )
        
        # Generate a public key for use in the exchange.
        asymmetric_public_key = private_key.public_key()

        # Serialize (and save) private key
        with open("public.pem", "wb") as file:
            file.write(asymmetric_public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo))

        return asymmetric_public_key
    except Exception as err:
        log.logger.debug(err, exc_info=True)
