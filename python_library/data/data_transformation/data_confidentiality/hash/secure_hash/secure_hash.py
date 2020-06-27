from pathlib import Path
from ppython_library.product_service.operations.event.script_logging import script_logging as log

from python_library.data.data_transformation.data_confidentiality.hash.secure_hash import secure_hash_algorithm
import hashlib

def secure_hash_def(data):
    try:
        secure_hash = secure_hash_algorithm.secure_hash_algorithm_def()
        secure_hash.update(data)
        return secure_hash
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)

