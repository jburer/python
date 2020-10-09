""" Identity Module """

from python_library.identity_and_access.identity import authenticate_identity_aws
from python_library.product_service.operations.log import log

class Identity:
    """ Identity Class """

    def __init__(self, id_attribute, data_classification):
        self.id_attribute = id_attribute
        self.data_classification = data_classification

    @classmethod
    def authenticate_identity(cls, identity):
        """ Authenticate Identity Function """

        # Input Policy

        # Test Against Policy

        # Authenticate Identity
        try:
            session = authenticate_identity_aws.authenticate_identity_aws_def(identity)

            if session is None:
                # Record Authentication Failure Event
                message = '{"App" : {"Authentication" : {"Response" : "Failure", "Profile" : "' + identity + '"}}}'
            else:
                # Record Authentication Success Event
                message = '{"App" : {"Authentication" : {"Response" : "Success", "Profile" : "' + identity + '"}}}'
            log.logger.info(message, exc_info=True)

            return session
        except Exception as err:
            log.logger.debug(err, exc_info=True)
            return None

