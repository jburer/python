""" Authentication Code Generation Module """

from hashlib import blake2b
from python_library.data.data_transformation.type_conversion import byte_conversion
from python_library.product_service.operations.event.log import log

def authentication_code_generation_def(data_in, key_in):
    """ Authentication Code Generation Function """

    data_as_bytes = byte_conversion.byte_conversion_def(data_in)

    try:
        authentication_code = blake2b(key=key_in, digest_size=16)
        authentication_code.update(data_as_bytes)
        return authentication_code.hexdigest()
    except Exception as err:
        log.logger.debug(err, exc_info=True)