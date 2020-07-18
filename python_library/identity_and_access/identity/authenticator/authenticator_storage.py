from datetime import datetime
from pathlib import Path
from python_library.product_service.operations.event.log import log

from app.models import AuthenticatorStorage 

from python_library.data.data_transformation.data_confidentiality.hash.secure_hash.derived_secure_hash import derived_secure_hash

def authenticator_storage_def(authenticator):
    
    my_derived_secure_hash = derived_secure_hash.derived_secure_hash_def(authenticator)
    
    try:
        AuthenticatorStorage.objects.create(store_date=datetime.now(), authenticator=my_derived_secure_hash)
        return
    except Exception as err:
        log.logger.debug(err, exc_info=True)