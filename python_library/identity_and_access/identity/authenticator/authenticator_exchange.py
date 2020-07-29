""" Authenticator Exchange """

from python_library.product_service.operations.event.log import log
#from python_library.identity_and_access.identity.authenticator.key import key_generation
from python_library.identity_and_access.identity.authenticator.key.shared_key import shared_key_generation
#from python_library.identity_and_access.identity.authenticator.key.asymmetric_key import asymmetric_key_generation
from python_library.data.data_transformation.data_confidentiality.encryption import encryption
from python_library.data.data_transformation.data_confidentiality.encryption import decryption

#TEMP authenticator storage
from python_library.identity_and_access.identity.authenticator import authenticator_storage

def authenticator_exchange_def(authenticator):
    """ Transfer the authenticator encrpyted """

    # Key generation
    #key = key_generation.key_generation_def()
    key = shared_key_generation.shared_key_generation_def()
    #key = asymmetric_key_generation.asymmetric_key_generation_def()

    # TEMP store key
    authenticator_storage.authenticator_storage_def(key)

    # Encryption
    ciphertext = encryption.encryption_def(key, authenticator)

    # Decryption
    authenticator = decryption.decryption_def(key, ciphertext)

    try:
        mykey = key
        return mykey, ciphertext, authenticator
    except Exception as err:
        log.logger.debug(err, exc_info=True)
