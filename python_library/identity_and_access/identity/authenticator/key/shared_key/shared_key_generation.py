""" Shared Key Generation (and Exchange) Module """

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

from python_library.product_service.operations.event.log import log
from python_library.identity_and_access.identity.authenticator.key.private_key import private_key_generation_dh
from python_library.identity_and_access.identity.authenticator.key.public_key import public_key_generation_dh

def shared_key_generation_def():
    """ Shared Key Generation Function (Using an Asymmetric Algorithm) """

    # Generate some parameters. These can be reused.
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

    # Generate Responder private key (just to make this work without interaction with another party)
    peer_private_key = parameters.generate_private_key() 

    # Receive public key
    peer_shared_public_key = peer_private_key.public_key()

    try:
        # Generate a private key for use in the exchange.
        private_key = private_key_generation_dh.private_key_generation_dh_def()

        # Generate a public key for use in the exchange.
        public_key = public_key_generation_dh.public_key_generation_def(private_key)

        # Send public key

        # Generate the shared key
        shared_key = private_key.exchange(peer_shared_public_key)
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
            backend=default_backend()
        ).derive(shared_key)

        derived_key = base64.urlsafe_b64encode(derived_key)

        return derived_key
    except Exception as err:
        log.logger.debug(err, exc_info=True)
