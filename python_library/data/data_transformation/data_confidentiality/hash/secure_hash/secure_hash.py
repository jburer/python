from pathlib import Path
from python_library.script_logging import script_logging as log

def secure_hash_def(data):
    try:
        secure_hash = data
        return secure_hash
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)

