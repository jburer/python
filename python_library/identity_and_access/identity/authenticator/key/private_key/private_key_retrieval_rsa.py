""" Private Key Retrieval Module using RSA """

from cryptography.hazmat.primitives import serialization
from python_library.product_service.operations.log import log

def private_key_retrieval_rsa_def():
    """ Private Key Retrieval Function using RSA """

    try:
        # Import private key
        with open("private.pem", "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
            )

        return private_key
    except Exception as err:
        log.logger.debug(err, exc_info=True)
