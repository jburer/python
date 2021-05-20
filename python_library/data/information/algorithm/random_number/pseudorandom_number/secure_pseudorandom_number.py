""" Secure Pseudorandom Number Module """

import secrets
from python_library.product_service.operations.log import log


def secure_pseudorandom_number_def(byte_size: int):
    """ Secure Pseudorandom Number Function """

    try:
        secure_pseudorandom_number = secrets.randbits(byte_size*8)
        return secure_pseudorandom_number
    except Exception as err:
        log.logger.debug(err, exc_info=True)
