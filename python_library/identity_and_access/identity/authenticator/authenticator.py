from pathlib import Path
from python.script_logging import script_logging as log

def authenticator_def(authenticator):
    try:
        as_authentiator = authenticator
        return as_authentiator
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)

authenticator_def('password')