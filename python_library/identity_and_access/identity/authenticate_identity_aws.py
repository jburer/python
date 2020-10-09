""" Authenticate Identity Module (for AWS) """

import boto3
import boto3.session
from botocore.exceptions import ProfileNotFound
from python_library.product_service.operations.log import log
from python_library.product_service.operations.log.event.event import Event

def authenticate_identity_aws_def(aws_profile):
    """ Authenticate Identity Function (for AWS) """

    # Input Policy

    # Test Against Policy

    # Authenticate Identity
    try:
        session = boto3.session.Session(profile_name=aws_profile)

        # Record Authentication Success Event
        message = '{"AWS" : {"Authentication" : {"Response" : "Success", "Profile" : "' + aws_profile + '"}}}'
        event_data = "{\"AuthenticationResponse\": \"Failure\"}"
        event = [{"Source": "app","DetailType": "AuthenticateIdentity","Detail": event_data}]
        log.logger.info(message, exc_info=True)

        events_client = Event.event_client(aws_profile)
        Event.create_event(events_client, aws_profile, event)

        return session
    except ProfileNotFound as err:
        # Record Authentication Failure Event
        message = '{"AWS" : {"Authentication" : {"Response" : "Failure", "Profile" : "' + aws_profile + '", "Error" : "ProfileNotFound", "Error Message" : "'
        log.logger.info('%s %s %s' % (message, err, '"}}}'), exc_info=True)

        return None
    except Exception as err:
        log.logger.debug(err, exc_info=True)
