from pathlib import Path
from python_library.product_service.operations.event.log import log
import hashlib

#authenticator
from python_library.identity_and_access.identity.authenticator import authenticator

#secure hash
from python_library.data.data_transformation.data_confidentiality.hash.secure_hash import secure_hash_algorithm

#salt, i.e. random number
from python_library.data.data_transformation.data_confidentiality.random_number import random_number as rn

#byte conversion
from python_library.data.data_transformation.type_conversion import byte_conversion


def derived_secure_hash_def(authenticator):

    #validate integrity of input

    #authorize execution

    #convert authenticator to bytes
    authenticator_as_bytes = byte_conversion.byte_conversion_def(authenticator)
    
    #establish secure hash algorithm (as str)
    secure_hash_algorithm_name = secure_hash_algorithm.secure_hash_algorithm_def()
    secure_hash_algorithm_name = str(secure_hash_algorithm_name.name)

    #establish random number and convert to bytes
    random_number = rn.random_number_def()
    random_number_as_bytes = byte_conversion.byte_conversion_def(random_number)

    #determine iterations
    iterations = 100000

    #determine derived key (dk) length (dklen)
    derived_secure_hash_length = None

    try:
        dk = hashlib.pbkdf2_hmac(secure_hash_algorithm_name, authenticator_as_bytes, random_number_as_bytes, iterations, derived_secure_hash_length)
        dk.hex()
        return dk.hex()
    except Exception as err:
        log.logger.debug(err, exc_info=True)

