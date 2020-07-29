""" Public Key Generation Module using Diffie-Hellman """

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh

from python_library.product_service.operations.event.log import log
from python_library.identity_and_access.identity.authenticator.key.private_key import private_key_generation_dh

def public_key_generation_def(private_key):
    """ Public Key Generation Function using Diffie-Hellman """

    try:
        # Generate a public key for use in the exchange.
        public_key = private_key.public_key()
        return public_key
    except Exception as err:
        log.logger.debug(err, exc_info=True)
