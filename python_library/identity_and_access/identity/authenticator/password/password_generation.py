""" Password Generation Module """
import secrets
import string
from python_library.product_service.operations.event.log import log

def password_generation_def():
    """ Password Generation Function """

    try:
        alphabet = string.ascii_letters + string.digits
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(10))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and sum(c.isdigit() for c in password) >= 3):
                break
        return password
    except Exception as err:
        log.logger.debug(err, exc_info=True)