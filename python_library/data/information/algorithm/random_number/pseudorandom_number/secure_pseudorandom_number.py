""" Secure Pseudorandom Number Module """

import secrets
import json
from python_library.product_service.operations.event.log import log

def secure_pseudorandom_number_def():
    """ Secure Pseudorandom Number Function """

    try:
        with open("./policy/policy.json", "r") as policy:
            policy_dict = json.load(policy)

        if policy_dict['policy']['secure_pseudorandom_number_byte_size']:
            secure_pseudorandom_number_byte_size = policy_dict['policy']['secure_pseudorandom_number_byte_size']
        else:
            secure_pseudorandom_number_byte_size = 32

        secure_pseudorandom_number = secrets.randbits(secure_pseudorandom_number_byte_size*8)
        return secure_pseudorandom_number
    except Exception as err:
        log.logger.debug(err, exc_info=True)