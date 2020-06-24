from pathlib import Path
from python.script_logging import script_logging as log

def get_bytes(in_bytes):   
    of_bytes = " as bytes is "

    try:
        in_bytes_as_int = int(in_bytes)
        is_bytes = in_bytes_as_int.to_bytes((in_bytes_as_int.bit_length() + 7) // 8, 'big')
        of_bytes += str(is_bytes)
        return is_bytes, of_bytes
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)

    try:
        is_bytes = in_bytes.encode('utf-8')
        of_bytes += str(is_bytes)
        return is_bytes, of_bytes
    except Exception as err:
        log.error_logging_def(err, Path(__file__).stem)
    