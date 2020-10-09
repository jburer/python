""" Authenticate Identity Module (for AWS) """

import boto3
import boto3.session
from botocore.exceptions import ProfileNotFound
from python_library.product_service.operations.event.log import log

def authenticate_identity_aws_def(aws_profile):
    """ Authenticate Identity Function (for AWS) """

    # Input Policy

    # Test Against Policy

    # Authenticate Identity
    try:
        session = boto3.session.Session(profile_name=aws_profile)

        # Record Authentication Success Event
        message = '{"AWS" : {"Authentication" : {"Response" : "Success", "Profile" : "' + aws_profile + '"}}}'
        log.logger.info(message, exc_info=True)

        return session
    except ProfileNotFound as err:
        # Record Authentication Failure Event
        message = '{"AWS" : {"Authentication" : {"Response" : "Failure", "Profile" : "' + aws_profile + '", "Error" : "ProfileNotFound", "Error Message" : "'
        log.logger.info('%s %s %s' % (message, err, '"}}}'), exc_info=True)

        return None
    except Exception as err:
        log.logger.debug(err, exc_info=True)
