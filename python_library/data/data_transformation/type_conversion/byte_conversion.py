from pathlib import Path
from python.script_logging import script_logging as log

def byte_conversion_def(in_bytes):   
    try:
        in_bytes_as_int = int(in_bytes)
        as_bytes = in_bytes_as_int.to_bytes((in_bytes_as_int.bit_length() + 7) // 8, 'big')
        return as_bytes
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)

    try:
        as_bytes = in_bytes.encode('utf-8')
        return as_bytes
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)
    