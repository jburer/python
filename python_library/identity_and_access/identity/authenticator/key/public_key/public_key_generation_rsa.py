""" Public Key Generation Module using RSA """

from cryptography.hazmat.primitives import serialization
from python_library.identity_and_access.identity.authenticator.key.private_key import private_key_retrieval_rsa
from python_library.product_service.operations.log import log

def public_key_generation_rsa_def():
    """ Public Key Generation Function using RSA """

    try:
        # Import private key
        private_key = private_key_retrieval_rsa.private_key_retrieval_rsa_def()
        
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
