""" Key Retrieval Module (from AWS) """

import logging
import base64

import boto3
import boto3.session

def retrieve_cmk(desc, aws_profile_name):
    """Retrieve an existing KMS CMK based on its description

    :param desc: Description of CMK specified when the CMK was created
    :return Tuple(KeyId, KeyArn) where:
        KeyId: CMK ID
        KeyArn: Amazon Resource Name of CMK
    :return Tuple(None, None) if a CMK with the specified description was
    not found
    """
    this_session=boto3.session.Session(profile_name=aws_profile_name)

    # Retrieve a list of existing CMKs
    # If more than 100 keys exist, retrieve and process them in batches
    kms_client = this_session.client('kms')
    try:
        response = kms_client.list_keys()
    except ClientError as e:
        logging.error(e)
        return None, None

    done = False
    while not done:
        for cmk in response['Keys']:
            # Get info about the key, including its description
            try:
                key_info = kms_client.describe_key(KeyId=cmk['KeyArn'])
            except ClientError as e:
                logging.error(e)
                return None, None

            # Is this the key we're looking for?
            if key_info['KeyMetadata']['Description'] == desc:
                return cmk['KeyId'], cmk['KeyArn']

        # Are there more keys to retrieve?
        if not response['Truncated']:
            # No, the CMK was not found
            logging.debug('A CMK with the specified description was not found')
            done = True
        else:
            # Yes, retrieve another batch
            try:
                response = kms_client.list_keys(Marker=response['NextMarker'])
            except ClientError as e:
                logging.error(e)
                return None, None

    # All existing CMKs were checked and the desired key was not found
    return None, None

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

    my_session=boto3.session.Session(profile_name=aws_profile_name)

    # Create data key
    kms_client = my_session.client('kms')
    try:
        response = kms_client.generate_data_key(KeyId=cmk_id, KeySpec=key_spec)
    except ClientError as e:
        logging.error(e)
        return None, None

    # Return the encrypted and plaintext data key
    return response['CiphertextBlob'], base64.b64encode(response['Plaintext'])