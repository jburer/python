""" Key Module """

#from cryptography.fernet import Fernet
from python_library.identity_and_access.identity.authenticator.key import create_key_asw
from python_library.product_service.operations.log import log

class Key:
    """ Key Class """

    def __init__(self, length, ttl):
        self.length = length
        self.ttl = ttl

    @classmethod
    def create_key(cls, client, identity):
        """ Create Key Function """

        # Input Policy

        # Test Against Policy

        # Create Key
        try:
            key = create_key_asw.create_data_key(client, identity)

            # Record Create Key Event
            if None in key:
                # Record Create Key Failure Event
                message = 'Create Key Failure:  ' + identity
            else:
                # Record Create Key Success Event
                message = 'Create Key Success:  ' + identity
            log.logger.info(message, exc_info=True)

            return key
        except Exception as err:
            log.logger.debug(err, exc_info=True)

        #return Fernet.generate_key()

    def encrypt_key(self):
        """ Encrypt Key Function """

        pass

    def decrypt_key(self):
        """ Decrypt Key Function """

        pass
