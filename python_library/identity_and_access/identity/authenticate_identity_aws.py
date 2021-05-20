""" Authenticate Identity Module (for AWS) """

import boto3
import boto3.session
from botocore.exceptions import ProfileNotFound
from python_library.product_service.operations.log import log

def authenticate_identity_aws_def(aws_profile):
    """ Authenticate Identity Function (for AWS) """

    # Input Policy

    # Test Against Policy

    # Authenticate Identity
    try:
        session = boto3.session.Session(profile_name=aws_profile)

        print('\n')
        print(session)
        print('\n')

        return session
    except ProfileNotFound as err:
        return 'Failure', err
    except Exception as err:
        # Log Bug 
        log.logger.debug(err, exc_info=True)
