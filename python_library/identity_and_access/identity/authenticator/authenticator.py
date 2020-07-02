from pathlib import Path
from python_library.product_service.operations.event.log import log

def authenticator_def(authenticator):
    try:
        authentiator = authenticator
        return authentiator
    except Exception as err:
        log.logger.debug(err, exc_info=True)

#authenticator_def('password')