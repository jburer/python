from cryptography.fernet import Fernet
from python_library.product_service.operations.event.log import log

class Key:


    def key_generation_def(self):

        try:
            key = Fernet.generate_key()
            return key
        except Exception as err:
            log.logger.debug(err, exc_info=True)