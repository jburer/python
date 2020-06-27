from pathlib import Path
from python_library.product_service.operations.event.script_logging import script_logging as log

import secrets

def random_number_def():   
    try:
        random_number = secrets.randbits(16*8)
        return random_number
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)