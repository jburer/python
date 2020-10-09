""" Event Module """

class Event:
    """ Event Class """

    def __init__(self, data_classification):
        self.data_classification = data_classification

    @classmethod
    def create_event(cls):
        """ Create Event Function """

        # Input Policy

        # Test Against Policy

        # Create Event
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