""" Key Retrieval Module """

from python_library.identity_and_access.identity.authenticator.key import retrieve_key_aws
from python_library.product_service.operations.event.log import log

def key_retrieval_def(key_description, profile_name):
    """ Key Retrieval Function """

    try:
        cmk = retrieve_key_aws.retrieve_cmk(key_description, profile_name)
        cmk_id = cmk[0]

        print('\n')
        print(cmk_id)
        print('\n')

        key = retrieve_key_aws.create_data_key(cmk_id, profile_name)
        
        print('\n')
        print(key)
        print('\n')

        return key
    except Exception as err:
        log.logger.debug(err, exc_info=True)
