from pathlib import Path
from python_library.product_service.operations.event.script_logging import script_logging as log

def authenticator_def(authenticator):
    try:
        authentiator = authenticator
        return authentiator
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)

authenticator_def('password')