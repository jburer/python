from pathlib import Path
from python_library.product_service.operations.event.log import log

def key_storage_def():

    try:
        key = Fernet.generate_key()
        return key
    except Exception as err:
        log.logger.debug(err, exc_info=True)