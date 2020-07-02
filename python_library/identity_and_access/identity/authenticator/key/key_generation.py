from pathlib import Path
from python_library.product_service.operations.event.log import log
from cryptography.fernet import Fernet

def key_generation_def():

    try:
        key = Fernet.generate_key()
        return key
    except Exception as err:
        log.logger.debug(err, exc_info=True)