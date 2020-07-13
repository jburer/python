from pathlib import Path
from python_library.product_service.operations.event.log import log

from python_library.identity_and_access.identity.authenticator.key import key_generation


def authenticator_exchange_def(authenticator):
    try:
        authentiator = authenticator
        return authentiator
    except Exception as err:
        log.logger.debug(err, exc_info=True)
