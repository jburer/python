from pathlib import Path
from python_library.product_service.operations.event.script_logging import script_logging as log

import hashlib

def secure_hash_algorithm_def():
    try:
        secure_hash_algorithm = hashlib.sha256()
        return secure_hash_algorithm
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)

