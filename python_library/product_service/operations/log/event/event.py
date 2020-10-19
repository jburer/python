""" Event Module """

import boto3
from python_library.product_service.operations.log.event import create_event_aws
from python_library.product_service.operations.log import log

class Event:
    """ Event Class """

    def __init__(self, data_classification):
        self.data_classification = data_classification

    @classmethod
    def event_client(cls):
        """ Event Client Function """

        session = boto3.session.Session(profile_name='User')
        if session is not None:
            return session.client('events')

    @classmethod
    def create_event(cls, client, identity, event):
        """ Create Event Function """

        # Input Policy

        # Test Against Policy

        # Create Event
        try:
            response = create_event_aws.put_events(client, identity, event)

            if response is None:
                # Record Authentication Failure Event
                message = '{"App" : {"Create Event" : {"Response" : "Failure", "Profile" : "' + identity + '"}}}'
            else:
                # Record Authentication Success Event
                message = '{"App" : {"Create Event" : {"Response" : "Success", "Profile" : "' + identity + '"}}}'
            log.logger.info(message, exc_info=True)

            return response
        except Exception as err:
            log.logger.debug(err, exc_info=True)
            return None
