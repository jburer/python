""" Encryption Module """


from python_library.product_service.operations.event.log import log
from python_library.data.data_transformation.type_conversion import byte_conversion

def encryption_def(key, data):
    """ Encryption Function """
    from cryptography.fernet import Fernet

    #create encrypted object
    encrypted_object = Fernet(key)

    #convert data to bytes
    data_as_bytes = byte_conversion.byte_conversion_def(data)

    try:
        ciphertext = encrypted_object.encrypt(data_as_bytes)
        return ciphertext
    except Exception as err:
        log.logger.debug(err, exc_info=True)