""" Secure Hash Algoritm Module -
Defines the hash algorithm to be used """

import hashlib
from python_library.product_service.operations.event.log import log

def secure_hash_algorithm_def():
    """  Secure Hash Algorithm Function """
    try:
        secure_hash_algorithm = hashlib.sha256()
        return secure_hash_algorithm
    except Exception as err:
        log.logger.debug(err, exc_info=True)
