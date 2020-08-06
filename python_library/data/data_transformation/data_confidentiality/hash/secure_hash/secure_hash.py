import hashlib
from python_library.product_service.operations.event.log import log
from python_library.data.data_transformation.data_confidentiality.hash.secure_hash import secure_hash_algorithm


def secure_hash_def(data):
    try:
        secure_hash = secure_hash_algorithm.secure_hash_algorithm_def()
        secure_hash.update(data)
        return secure_hash
    except Exception as err:
        log.logger.debug(err, exc_info=True)

