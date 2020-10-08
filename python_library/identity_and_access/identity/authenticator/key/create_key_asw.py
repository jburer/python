""" Create Key Module (AWS) """

import logging
import base64
from botocore.exceptions import ClientError
from python_library.identity_and_access.identity import authenticate_identity
from python_library.product_service.operations.event.log import log

def create_data_key(cmk_id, aws_profile_name, key_spec='AES_256'):
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

    # Test Against Policy

    # Authenticate Identity
    session = authenticate_identity.authenticate_identity_def('User2')

    # Connect to service
    kms_client = session.client('kms')

    # Create data key
    try:
        response = kms_client.generate_data_key(KeyId=cmk_id, KeySpec=key_spec)

        print('\n')
        #print(response)
        print('\n')

    except ClientError as err:

        print('\n')
        logging.error(err)
        print('\n')

        if err.response['Error']['Code'] == 'AccessDeniedException':
            log.logger.debug(err, exc_info=True)
            logging.error(err)
        else:
            raise err
        return None, None
    
    

    # Return the encrypted and plaintext data key
    return response['CiphertextBlob'], base64.b64encode(response['Plaintext'])