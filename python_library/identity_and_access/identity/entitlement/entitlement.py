""" Entitlement Module """

import boto3
from python_library.product_service.operations.log import log

class Entitlement:
    """ Entitlement Class """

    def __init__(self, permission, data_classification):
        self.permission = permission
        self.data_classification = data_classification

    @classmethod
    def authorize_entitlement(cls, identity):
        """ Authorize Entitlement Function """

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

