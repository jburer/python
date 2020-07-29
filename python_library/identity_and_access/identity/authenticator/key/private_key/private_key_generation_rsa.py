""" Private Key Generation Module using RSA """

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from python_library.product_service.operations.event.log import log

# Generate (Responder's) Public Key (just to test this locally)
#peer_asymmetric_private_key = rsa.generate_private_key(
#    public_exponent=65537,
#    key_size=2048,
#    backend=default_backend()
#)
#peer_asymmetric_public_key = peer_asymmetric_private_key.public_key()
#with open("public.pem", "wb") as file:
#    file.write(peer_asymmetric_public_key.public_bytes(
#        encoding=serialization.Encoding.PEM,
#        format=serialization.PublicFormat.PKCS1)
#    )

def private_key_generation_rsa_def():
    """ Private Key Generation Function using RSA """

    try:
        # Generate a private key for use in the exchange.
        asymmetric_private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        # Serialize (and save) private key
        with open("private.pem", "wb") as file:
            file.write(asymmetric_private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()))

        return asymmetric_private_key
    except Exception as err:
        log.logger.debug(err, exc_info=True)
