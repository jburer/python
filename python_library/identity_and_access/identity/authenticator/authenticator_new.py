from pathlib import Path
from python_library.product_service.operations.event.log import log

class Authenticator:

    def authenticator_generation_def(self):
        try:
            authentiator = 'password'
            return authentiator
        except Exception as err:
            log.logger.debug(err, exc_info=True)

    def authenticator_storage_def(self, authenticator):
        try:
            authentiator = authenticator
            return authentiator
        except Exception as err:
            log.logger.debug(err, exc_info=True)

    def authenticator_exchange_def(self, authenticator):
        try:
            authentiator = authenticator
            return authentiator
        except Exception as err:
            log.logger.debug(err, exc_info=True)
