from pathlib import Path

from cryptography.fernet import Fernet

from python_library.product_service.operations.event.log import log
from python_library.data.data_transformation.type_conversion import byte_conversion

def decryption_def(key, ciphertext):

    #create decrypted object
    data = Fernet(key)

    #convert data to bytes
    if type(ciphertext) is bytes:
        data_as_bytes = ciphertext
    else:
        data_as_bytes = byte_conversion.byte_conversion_def(ciphertext)

    try:
        data = data.decrypt(data_as_bytes)
        return data
    except Exception as err:
        log.logger.debug(err, exc_info=True)