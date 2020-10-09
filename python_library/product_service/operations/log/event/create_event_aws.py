""" Create Event Module (AWS) """

from botocore.exceptions import ClientError
from python_library.product_service.operations.log import log

def put_events(events_client, aws_profile, event):
    """  Sends custom events to Amazon EventBridge so that they
    can be matched to rules.  """

    # Input Policy

    # Test Against Policy

    # Create Event
    try:
        response = events_client.put_events(Entries=event)

         # Record Authorization Success Event
        message = '{"AWS" : {"Authorization" : {"Response" : "Success", "Profile" : "' + aws_profile + '"}}}'
        log.logger.info(message, exc_info=True)

        # Record Create Event Success Event
        message = '{"AWS" : {"Create Event" : {"Response" : "Success", "Profile" : "' + aws_profile + '", "Response Message" : "' + response + '"}}}'
        log.logger.info(message, exc_info=True)

    except ClientError as err:
        # Record Authorization Failure Event
        if err.response['Error']['Code'] == 'AccessDeniedException':
            message = '{"AWS" : {"Authorization" : {"Response" : "Failure", "Profile" : "' + aws_profile + '", "Error" : "AccessDeniedException", "Error Message" : "'
            log.logger.info('%s %s %s' % (message, err, '"}}}'), exc_info=True)
        else:
            raise err
        return None, None
