""" Private Key Generation Module using Diffie-Hellman """

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh

from python_library.product_service.operations.event.log import log

def private_key_generation_dh_def():
    """ Private Key Generation Function (Using an Asymmetric Algorithm) """

    # Generate some parameters. These can be reused.
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

    try:
        # Generate a private key for use in the exchange.
        shared_private_key = parameters.generate_private_key()

        return shared_private_key
    except Exception as err:
        log.logger.debug(err, exc_info=True)
