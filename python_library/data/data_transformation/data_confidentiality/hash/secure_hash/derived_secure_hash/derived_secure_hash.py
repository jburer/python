from pathlib import Path
from python_library.product_service.operations.event.script_logging import script_logging as log
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

    print(authenticator)

    #convert authenticator to bytes
    authenticator_as_bytes = byte_conversion.byte_conversion_def(authenticator)
    print(authenticator_as_bytes)
    
    #establish secure hash algorithm (as str)
    secure_hash_algorithm_name = secure_hash_algorithm.secure_hash_algorithm_def()
    secure_hash_algorithm_name = str(secure_hash_algorithm_name.name)
    print(secure_hash_algorithm_name)

    #establish random number and convert to bytes
    random_number = rn.random_number_def()
    print(random_number)
    random_number_as_bytes = byte_conversion.byte_conversion_def(random_number)
    print(random_number_as_bytes)

    #determine iterations
    iterations = 100000

    #determine derived key (dk) length (dklen)
    derived_secure_hash_length = None

    try:
        dk = hashlib.pbkdf2_hmac(secure_hash_algorithm_name, authenticator_as_bytes, random_number_as_bytes, iterations)
        dk.hex()
        print(dk)
        print(dk.hex())
        return dk.hex()
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)

