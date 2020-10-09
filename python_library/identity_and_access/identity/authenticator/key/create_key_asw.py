""" Create Key Module (AWS) """

import base64
from botocore.exceptions import ClientError
from python_library.product_service.operations.event.log import log

def create_data_key(kms_client, aws_profile):
    """Generate a data key to use when encrypting and decrypting data

    :param cmk_id: KMS CMK ID or ARN under which to generate and encrypt the
    data key.
    :param key_spec: Length of the data encryption key. Supported values:
        'AES_128': Generate a 128-bit symmetric key
        'AES_256': Generate a 256-bit symmetric key
    :return Tuple(EncryptedDataKey, PlaintextDataKey) where:
        EncryptedDataKey: Encrypted CiphertextBlob data key as binary string
        PlaintextDataKey: Plaintext base64-encoded data key as binary string
    :return Tuple(None, None) if error
    """

    # Input Policy
    key_spec='AES_256'
    cmk_id = 'c7004d4e-a313-4c6f-9999-893f6c3e068f'

    # Test Against Policy

    # Create Data Key
    try:
        response = kms_client.generate_data_key(KeyId=cmk_id, KeySpec=key_spec)

        # Record Authorization Success Event
        message = '{"AWS" : {"Authorization" : {"Response" : "Success", "Profile" : "' + aws_profile + '"}}}'
        log.logger.info(message, exc_info=True)

        # Record Create Key Event
        message = '{"AWS" : {"Create Key" : {"Response" : "Success", "Profile" : "' + aws_profile + '"}}}'
        log.logger.info(message, exc_info=True)

    except ClientError as err:
        # Record Authorization Failure Event
        if err.response['Error']['Code'] == 'AccessDeniedException':
            message = '{"AWS" : {"Authorization" : {"Response" : "Failure", "Profile" : "' + aws_profile + '", "Error" : "AccessDeniedException", "Error Message" : "'
            log.logger.info('%s %s %s' % (message, err, '"}}}'), exc_info=True)
        else:
            raise err
        return None, None

    # Return the encrypted and plaintext data key
    return response['CiphertextBlob'], base64.b64encode(response['Plaintext'])