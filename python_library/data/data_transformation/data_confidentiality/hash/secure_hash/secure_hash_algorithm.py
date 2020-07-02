from pathlib import Path
from python_library.product_service.operations.event.log import log

import hashlib

def secure_hash_algorithm_def():
    try:
        secure_hash_algorithm = hashlib.sha256()
        return secure_hash_algorithm
    except Exception as err:
        log.logger.debug(err, exc_info=True)

