""" Key Generation Module """

from python_library.product_service.operations.event.log import log

def key_generation_def():
    """ Key Generation Function """

    try:
        from cryptography.fernet import Fernet
        key = Fernet.generate_key()
        return key
    except Exception as err:
        log.logger.debug(err, exc_info=True)
