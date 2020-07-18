""" Aymmetric Key Generation (and Exchange) Module """

from cryptography.hazmat.backends import default_backend
#from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
#from cryptography.hazmat.primitives.kdf.hkdf import HKDF

from python_library.product_service.operations.event.log import log

#Generate Public Key (just to test this locally)
peer_asymmetric_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend())
peer_asymmetric_public_key = peer_asymmetric_private_key.public_key()
with open("public.pem", "wb") as file:
    file.write(peer_asymmetric_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1))

def asymmetric_key_generation_def():
    """ Aymmetric Key Generation Function """

    try:
        # Generate a private key for use in the exchange.
        asymmetric_private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend())

        # Generate a public key for use in the exchange.
        asymmetric_public_key = asymmetric_private_key.public_key()

        #send public key

        #receive public key
        #peer_symmetric_public_key = peer_private_key.public_key()

        # Generate the symmetric key .
        #symmetric_key = symmetric_private_key.exchange(peer_symmetric_public_key)
        return asymmetric_private_key, asymmetric_public_key #, symmetric_key
    except Exception as err:
        log.logger.debug(err, exc_info=True)