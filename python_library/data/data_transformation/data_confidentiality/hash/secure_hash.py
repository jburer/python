""" Secure Hash Module """

import hashlib
from python_library.product_service.operations.log import log
from python_library.data.data_transformation.type_conversion import byte_conversion


def secure_hash_def(algorithm, data):
    """ Secure Hash Function """

    try:
        data_as_bytes = byte_conversion.byte_conversion_def(data)
        secure_hash = hashlib.new(algorithm, data_as_bytes)
        secure_hash.update(data_as_bytes)
        return secure_hash.digest(), secure_hash.name, secure_hash.hexdigest()
    except Exception as err:
        log.logger.debug(err, exc_info=True)
