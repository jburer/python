""" Authenticate Identity Module """

from python_library.identity_and_access.identity import authenticate_identity_aws
from python_library.product_service.operations.event.log import log

def authenticate_identity_def(identity):
    """ Authenticate Identity Function """

    # Input Policy

    # Test Against Policy

    # Authenticate Identity
    try:
        session = authenticate_identity_aws.authenticate_identity_aws_def(identity)

        if session is None:
            # Record Authentication Failure Event
            message = 'Authentication Failure:  ' + identity
        else:
            # Record Authentication Success Event
            message = 'Authentication Success:  ' + identity
        log.logger.info(message, exc_info=True)

        return session
    except Exception as err:
        log.logger.debug(err, exc_info=True)
