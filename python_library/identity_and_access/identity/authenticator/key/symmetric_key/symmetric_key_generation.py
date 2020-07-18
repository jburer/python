""" Symmetric Key Generation (and Exchange) Module """

from cryptography.hazmat.backends import default_backend
#from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
#from cryptography.hazmat.primitives.kdf.hkdf import HKDF

from python_library.product_service.operations.event.log import log

def symmetric_key_generation_def():
    """ Symmetric Key Generation Function (Using an Asymmetric Algorithm) """

    # Generate some parameters. These can be reused.
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

    try:
        # Generate a private key for use in the exchange.
        symmetric_private_key = parameters.generate_private_key()
        
        peer_private_key = parameters.generate_private_key() #just to make this work

        # Generate a public key for use in the exchange.
        symmetric_public_key = symmetric_private_key.public_key()

        #send public key

        #receive public key
        peer_symmetric_public_key = peer_private_key.public_key()

        # Generate the symmetric key .
        symmetric_key = symmetric_private_key.exchange(peer_symmetric_public_key)
        return symmetric_private_key, symmetric_public_key, symmetric_key
    except Exception as err:
        log.logger.debug(err, exc_info=True)
