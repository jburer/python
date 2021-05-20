""" Identity Module """

import boto3
from python_library.identity_and_access.identity import authenticate_identity_aws
from python_library.product_service.operations.log.event.event import Event
from python_library.product_service.operations.log import log

class Identity:
    """ Identity Class """

    def __init__(self, id_attribute, data_classification):
        self.id_attribute = id_attribute
        self.data_classification = data_classification

    @classmethod
    def identity_client(cls, identity):
        """ Identity Client Function """

        session = boto3.session.Session(profile_name=identity)
        if session is not None:
            return session.client('iam')

    @classmethod
    def authenticate_identity(cls, identity):
        """ Authenticate Identity Function """

        # Input Policy

        # Test Against Policy

        # Authenticate Identity
        try:
            session = authenticate_identity_aws.authenticate_identity_aws_def(identity)

            print('\n')
            print(session)
            print('\n')

            # Create Event
            #if 'Failure' in session:
            #    status = 'Failure'
            #else:
            #    status = 'Success'

            #print('\n')
            #print(status)
            #print('\n')

            #event_data = ('"App" : {' +
                          #'"Identity" : {' + 
                          #'"Id" : "' + identity + '", ' +
                          #'"Authentication" : {' +
                          #'"Status" : "' + status + '", ' +
                          #'"Response" : "ProfileNotFound"}}}')

            #print('\n')
            #print(event_data)
            #print(type(event_data))
            #print('\n')

            #event_trigger = '{\'AuthenticationResponse\': \'' + status + '\',' + event_data + '}'
            #event_trigger = "{\"AuthenticationResponse\": \"" + status + "\", " + event_data + "}"
            #event_trigger = "{\"AuthenticationResponse\": \"" + status + "\"}"

            #print('\n')
            #print(event_trigger)
            #print(type(event_trigger))
            #print('\n')

            #event = [{"Source": "app", "DetailType": "AuthenticateIdentity", "Detail": event_trigger}]

            #print('\n')
            #print(event)
            #print(type(event))
            #print('\n')

            #events_client = Event.event_client()
            #Event.create_event(events_client, identity, event)

            # Log Event
            #log.logger.info('%s %s %s' % (message, err, '"}}}'), exc_info=True)
            #log.logger.info(event_data, exc_info=True)

            return session
        except Exception as err:
            log.logger.debug(err, exc_info=True)
            return None

