from pathlib import Path
from python_library.product_service.operations.event.log import log

#encryption
from cryptography.fernet import Fernet

#key
from python_library.identity_and_access.identity.authenticator.key import key_generation

#byte conversion
from python_library.data.data_transformation.type_conversion import byte_conversion

def encryption_def(data):

    #generate key (as bytes)
    mykey = key_generation.key_generation_def()

    #create encrypted object
    encrypted_object = Fernet(mykey)

    #convert data to bytes
    data_as_bytes = byte_conversion.byte_conversion_def(data)

    try:
        ciphertext = encrypted_object.encrypt(data_as_bytes)
        return ciphertext
    except Exception as err:
        log.logger.debug(err, exc_info=True)