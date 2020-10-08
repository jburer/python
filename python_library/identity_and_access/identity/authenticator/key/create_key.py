""" Create Key Module """

#from cryptography.fernet import Fernet
from python_library.identity_and_access.identity.authenticator.key import create_key_asw
from python_library.product_service.operations.event.log import log

def create_key_def():
    """ Create Key Function """

    #input policy

    #test policy

    cmk_id = 'c7004d4e-a313-4c6f-9999-893f6c3e068f'

    try:
        #key = Fernet.generate_key()
        key = create_key_asw.create_data_key( cmk_id, 'User2')

        print('\n')
        #print(key)
        print('\n')

        return key
    except Exception as err:
        log.logger.debug(err, exc_info=True)
